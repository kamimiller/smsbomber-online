from flask import render_template,redirect,url_for,session
from bomber import process
from sms_bomber import app
from sms_bomber.forms import EnterNumber

# -------------------- # Base Project Routes #-------------------- #

@app.route("/",methods=["POST","GET"])
def home():
    form = EnterNumber()
    if form.validate_on_submit():
        session["task"] = {
            "task_id" : process.createBomber(form.number.data).name,
            "target" : form.number.data,
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
    return render_template("sms.html",task_id=session.get("task")["task_id"])

@app.route("/send/<id_task>")
def send(id_task):
    process.startBomber(id_task)
    return render_template("send.html", number=session.get("task")["target"])

@app.route("/stop")
def stop():
    process.stopBomber(session.get("task")["task_id"])
    return "Stoped !!"

# -------------------- # Panel # -------------------- #

@app.route("/account")
def account():return render_template("account.html")

# -------------------- # tract # -------------------- #

@app.route("/tract")
def tract():return render_template("tract.html")
