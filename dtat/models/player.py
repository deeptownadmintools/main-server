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
    level = Column(Integer, default=0)
    depth = Column(Integer, default=0)
    mine = Column(Integer, default=0)
    chemMine = Column(Integer, default=0)
    oil = Column(Integer, default=0)
    crafters = Column(Integer, default=0)
    smelters = Column(Integer, default=0)
    lastEventDonation = Column(Integer, default=0)

    def __init__(self, guild_id, name, rockbiteId, lastOnline=None,
                 level=None, depth=None, mine=None, chemMine=None, oil=None,
                 crafters=None, smelters=None, lastEventDonation=None):
        self.guild_id = guild_id
        self.name = name
        self.rockbiteId = rockbiteId
        if lastOnline is not None:
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

    @staticmethod
    def keys():
        return [
            'id',
            'name',
            'lastOnline',
            'level',
            'depth',
            'mine',
            'chemMine',
            'oil',
            'crafters',
            'smelters',
            'lastEventDonation',
        ]

    def list(self):
        return [
            self.id,
            self.name,
            self.lastOnline,
            self.level,
            self.depth,
            self.mine,
            self.chemMine,
            self.oil,
            self.crafters,
            self.smelters,
            self.lastEventDonation,
        ]
