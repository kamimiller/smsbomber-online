from sms_bomber import app
from datetime import datetime
from sms_bomber.models import Database

if __name__ == '__main__':
    
    db = Database()
    
    db.addRedeem("rootRedeem",datetime.now().timestamp())    
    # app.run(debug=True)