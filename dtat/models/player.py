from dtat.app import db


class Player(db.Model):
    __tablename__ = "player"
    guild_id = db.Column(db.Integer, db.ForeignKey("guild.id"))
    counts = db.relationship('Count', backref='player', lazy=True)
    name = db.Column(db.String(32), nullable=False)
    rockbiteID = db.Column(db.String(24))
    lastOnline = db.Column(db.DateTime)
    level = db.Column(db.Integer)
    depth = db.Column(db.Integer)
    mine = db.Column(db.Integer)
    chemMine = db.Column(db.Integer)
    oil = db.Column(db.Integer)
    crafters = db.Column(db.Integer)
    smelters = db.Column(db.Integer)
    lastEventDonation = db.Column(db.Integer)
