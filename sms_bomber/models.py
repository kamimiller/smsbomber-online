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
        
        self.connection.commit()
        self.connection.close()
        return False
    
    def getInfoRedeemAll(self):
        data = []
        self.cursor.execute("SELECT * FROM redeem")
        for i in self.cursor.fetchall():
            data.append(
                {
                    "redeem_code" : i[0],
                    "date_start" : datetime.fromtimestamp(i[1]).strftime("%m/%d/%Y"),
                    "date_end" : datetime.fromtimestamp(i[2]).strftime("%m/%d/%Y"),
                }
            )   
            
        self.connection.commit()
        self.connection.close()
        return data

    def getInfoRedeem(self,redeem):
        self.cursor.execute(f"SELECT * FROM redeem WHERE redeem_code = '{redeem}'")
        redeem_info = self.cursor.fetchone()
        self.connection.commit()
        self.connection.close()
        return {
            "redeem_code" : redeem_info[0],
            "date_start" : redeem_info[1],
            "date_end" : redeem_info[2],
        }
        
    
    def addRedeem(self,redeem,date):
        self.cursor.execute(f"INSERT INTO redeem VALUES ('{redeem}','{datetime.now().timestamp()}','{date}')")
        self.connection.commit()
        self.connection.close()
        
    def deleteRedeem(self,redeem):
        self.cursor.execute(f"DELETE FROM redeem WHERE redeem_code = '{redeem}'")
        self.connection.commit()
        self.connection.close()