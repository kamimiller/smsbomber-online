import sqlite3
from datetime import datetime

class Database:
    
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
    
    def checkRedeem(self,redeem):
        self.cursor.execute(f"SELECT * FROM redeem WHERE redeem_code='{redeem}'")
        res_redeem = self.cursor.fetchall()
        
        if res_redeem != []:
            return True
        
        self.connection.close()
        return False
    
    def getInfoRedeem(self,redeem):
        pass
    
    def addRedeem(self,redeem,date):
        self.cursor.execute(f"INSERT INTO redeem VALUES ('{redeem}','{datetime.now().timestamp()}','{date}')")
        self.connection.commit()
        self.connection.close()