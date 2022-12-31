from flask import render_template,redirect,url_for,session,request
from sms_bomber import app
from bomber import process
from sms_bomber.forms import EnterNumber, Login, Redeem
from sms_bomber.models import Database
from datetime import datetime

# -------------------- # Base Project Routes #-------------------- #

@app.route("/",methods=["POST","GET"])
def home():
    form = EnterNumber()
    if form.validate_on_submit():
        session["task"] = {
            "target": form.number.data
        }
        if form.redeem:
            db = Database()
            if db.checkRedeem(form.redeem.data):
                session["task"]["redeem"] = form.redeem.data
        
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
            if session["task"]["redeem"]:
                db = Database()
                if db.checkRedeem(session.get("task")["redeem"]):
                    db = Database()
                    if db.getInfoRedeem(session["task"]["redeem"])["date_end"] >= datetime.now().timestamp():
                        process.startBomberVip(target)
                        return render_template("send.html", number=target, vip_mode=True)
                    return redirect(url_for('home'))
                
            process.startBomber(target)
            return render_template("send.html", number=target)
        
    except TypeError:
        return "this task id not currect or finished bomber process"
    
    return "this task id not currect"

# ------------------- # Panel Admin # ------------------- #

@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = Login()
    form_redeem = Redeem()
    if form.validate_on_submit():
        if form.username.data == "smsbombe" and form.password.data == "GC087)ltF+oc9J":
            db = Database()
            redeems = db.getInfoRedeemAll()
            return render_template('panel.html',form=form_redeem, redeems=redeems, date=datetime.now().strftime("%m/%d/%Y"))
        
    return render_template('admin.html', form=form)

@app.route("/admin/new", methods=["POST"])
def new():
    db = Database()
    if request.form["redeem"] and request.form["date_end"]:
        redeem = request.form["redeem"]
        date_end:str = request.form["date_end"]
        if not db.checkRedeem(redeem):
            res_date = date_end.split("-")
            date = datetime(int(res_date[0]), int(res_date[1]), int(res_date[2]))
            db = Database()
            db.addRedeem(redeem, date.timestamp())
            
            return redirect(url_for('admin'))
    
        return "this alredy redeem is available"  
    
    return "Error"  
            
@app.route("/admin/delete/<redeem>", methods=["GET"])
def delete(redeem):
    db = Database()
    db.deleteRedeem(redeem)
    
    db = Database()
    if not db.checkRedeem(redeem):
        return redirect(url_for('admin'))
    
    return "Error"
