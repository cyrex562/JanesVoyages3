from app import db


class Voyage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))
    ship = db.relationship('Ship',
                           backref=db.backref('voyages', lazy=True))


class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    captain_id = db.Column(db.Integer, db.ForeignKey('captain.id'))
    captain = db.relationship('Captain',
                              backref=db.backref('ships', lazy=True))
    flag_id = db.Column(db.Integer, db.ForeignKey('flag.id'))
    flag = db.relationship('Flag')


class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String, nullable=False)