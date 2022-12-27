from sms_bomber import app
from datetime import datetime
from sms_bomber.models import Database

if __name__ == '__main__':
    
    db = Database()
    
    app.run(debug=True)