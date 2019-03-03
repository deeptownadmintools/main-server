from dtat.app import db


class Count(db.Model):
    __tablename__ = "count"
    timestamp_id = db.Column(db.Integer, db.ForeignKey("timestamp.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"))
    donated = db.Column(db.BigInteger)
    received = db.Column(db.BigInteger)
