from dtat.app import db


class Guild(db.Model):
    __tablename__ = "guild"
    name = db.Column(db.String(32), nullable=False)
    timeStamps = db.relationship('TimeStamp', backref='guild', lazy=True)
    rockbiteID = db.Column(db.String(24))
    totalLevel = db.Column(db.Integer)
    totalDonations = db.Column(db.BigInteger)
