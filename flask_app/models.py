from app import db

class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)

    username = db.Column(db.String(64) ,index=True,unique=True)
    fullname = db.Column(db.String(100) ,index=True,unique=True)
    email = db.Column(db.String(120) ,index=True,unique=True)

    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = password

    def check_password(self,password):
        return self.password_hash

    def getJsonData(self):
        return {"username" : self.username , 
                "fullname" : self.fullname , 
                "email" : self.email }
    
