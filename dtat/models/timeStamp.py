from dtat.app import db


class TimeStamp(db.Model):
    __tablename__ = "timestamp"
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"))
    counts = db.relationship('Count', backref='timestamp', lazy=True)
    date = db.Column(db.DateTime)
