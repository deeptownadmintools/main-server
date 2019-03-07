from dtat import app
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from datetime import datetime


class Player(app.db.Model):
    __tablename__ = "player"
    guild_id = Column(Integer, ForeignKey("guild.id"))
    counts = app.db.relationship('Count', backref='player', lazy=True)
    name = Column(String(32), nullable=False)
    rockbiteId = Column(String(24), nullable=False, unique=True)
    lastOnline = Column(DateTime)
    level = Column(Integer)
    depth = Column(Integer)
    mine = Column(Integer)
    chemMine = Column(Integer)
    oil = Column(Integer)
    crafters = Column(Integer)
    smelters = Column(Integer)
    lastEventDonation = Column(Integer)

    def __init__(self, guild_id, name, rockbiteId, lastOnline, level, depth,
                 mine, chemMine, oil, crafters, smelters, lastEventDonation):
        self.guild_id = guild_id
        self.name = name
        self.rockbiteId = rockbiteId
        self.lastOnline = datetime.strptime(
            lastOnline,
            "%Y-%m-%dT%H:%M:%S.%fZ")
        self.level = level
        self.depth = depth
        self.mine = mine
        self.chemMine = chemMine
        self.oil = oil
        self.crafters = crafters
        self.smelters = smelters
        self.lastEventDonation = lastEventDonation
