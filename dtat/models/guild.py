from dtat import app
from sqlalchemy import Column, Integer, String, DateTime


class Guild(app.db.Model):
    """
    Database model representing guilds.
    """
    __tablename__ = "guild"
    name = Column(String(32), nullable=False)
    timeStamps = app.db.relationship('TimeStamp', backref='guild', lazy=True)
    players = app.db.relationship('Player', backref='guild', lazy=True)
    rockbiteId = Column(String(32), nullable=False, unique=True)
    level = Column(Integer)
    lastVisited = Column(DateTime)

    def __init__(self, name, rockbiteId, level):
        self.name = name
        self.rockbiteId = rockbiteId
        self.level = level

    @staticmethod
    def keys():
        return [
            'id',
            'name',
            'level',
        ]

    def list(self):
        return [
            self.id,
            self.name,
            self.level,
        ]
