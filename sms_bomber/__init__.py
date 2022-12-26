from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "9d1f9b456d70aab31aac146753da5bba"

from sms_bomber import routes