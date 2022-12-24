from sms_bomber import db
from threading import Thread

tasks = {}

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_task = db.Column(db.String(255), unique=True, nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.id_task}, {self.number}, {self.status})"
    
class Database:
    tasks = {}
    def __init__(self):
        pass
    
    def addBomb(self,token_hex):
        pass
    
    def stopBomb(self):pass