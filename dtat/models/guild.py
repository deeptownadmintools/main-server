from dtat import app


class Guild(app.db.Model):
    __tablename__ = "guild"
    name = app.db.Column(app.db.String(32), nullable=False)
    timeStamps = app.db.relationship('TimeStamp', backref='guild', lazy=True)
    rockbiteID = app.db.Column(app.db.String(24))
    totalLevel = app.db.Column(app.db.Integer)
    totalDonations = app.db.Column(app.db.BigInteger)
