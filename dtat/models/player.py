from dtat import app


class Player(app.db.Model):
    __tablename__ = "player"
    guild_id = app.db.Column(app.db.Integer, app.db.ForeignKey("guild.id"))
    counts = app.db.relationship('Count', backref='player', lazy=True)
    name = app.db.Column(app.db.String(32), nullable=False)
    rockbiteID = app.db.Column(app.db.String(24))
    lastOnline = app.db.Column(app.db.DateTime)
    level = app.db.Column(app.db.Integer)
    depth = app.db.Column(app.db.Integer)
    mine = app.db.Column(app.db.Integer)
    chemMine = app.db.Column(app.db.Integer)
    oil = app.db.Column(app.db.Integer)
    crafters = app.db.Column(app.db.Integer)
    smelters = app.db.Column(app.db.Integer)
    lastEventDonation = app.db.Column(app.db.Integer)
