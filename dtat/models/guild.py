from dtat import app
from sqlalchemy import Column, Integer, String, DateTime


class Guild(app.db.Model):
    __tablename__ = "guild"
    name = Column(String(32), nullable=False)
    timeStamps = app.db.relationship('TimeStamp', backref='guild', lazy=True)
    rockbiteId = Column(String(32), nullable=False, unique=True)
    level = Column(Integer)
    lastVisited = Column(DateTime)

    def __init__(self, name, rockbiteId, level):
        self.name = name
        self.rockbiteId = rockbiteId
        self.level = level
