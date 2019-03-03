from dtat import app


class TimeStamp(app.db.Model):
    __tablename__ = "timestamp"
    player_id = app.db.Column(app.db.Integer, app.db.ForeignKey("player.id"))
    counts = app.db.relationship('Count', backref='timestamp', lazy=True)
    date = app.db.Column(app.db.DateTime)
