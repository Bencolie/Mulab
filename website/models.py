from website import db

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    link = db.Column(db.String(8000))
    tracks = db.relationship('Tracks')


class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    dlink = db.Column(db.String(8000))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
