from website import db

class Tracks(db.Model):
    __tablename__ = 'MTracks'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    dlink = db.Column(db.String(8000))