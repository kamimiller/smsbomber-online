from flask import render_template,redirect,url_for,session
from sms_bomber import app
from bomber import process
from sms_bomber.forms import EnterNumber
from secrets import token_hex

# -------------------- # Base Project Routes #-------------------- #

@app.route("/",methods=["POST","GET"])
def home():
    form = EnterNumber()
    if form.validate_on_submit():
        session["task"] = {
            "target": form.number.data
        }
        
        return redirect(url_for("sms"))
    return render_template("home.html", form=form)

@app.route("/about")
def about():return render_template("about.html")

@app.route("/privacy")
def privacy():return render_template("privacy.html")

@app.route("/terms")
def terms():return render_template("terms.html")

@app.route("/contect")
def contact():return render_template("contact.html")

# -------------------- # Sms Bomber # -------------------- #

@app.route("/sms", methods=["GET"])
def sms():
    return render_template("sms.html",task_id=session.get("task")["target"])

@app.route("/send/<target>")
def send(target):
    try:
        if session.get("task")["target"]:
            process.startBomber(target)
            return render_template("send.html", number=target)
    except TypeError:
        return "this task id not currect or finished bomber process"
    
    return "this task id not currect"
