from dtat import app


class Count(app.db.Model):
    __tablename__ = "count"
    timestamp_id = app.db.Column(app.db.Integer, app.db.ForeignKey("timestamp.id"))
    player_id = app.db.Column(app.db.Integer, app.db.ForeignKey("player.id"))
    donated = app.db.Column(app.db.BigInteger)
    received = app.db.Column(app.db.BigInteger)
