from dtat import app
from sqlalchemy import Column, Integer, BigInteger, String, LargeBinary


class Guild(app.db.Model):
    __tablename__ = "guild"
    name = Column(String(32), nullable=False)
    timeStamps = app.db.relationship('TimeStamp', backref='guild', lazy=True)
    # rockbiteID = Column(LargeBinary(length=96),unique=True)
    rockbiteID = Column(String(32), nullable=False, unique=True)
    # totalLevel = Column(Integer)
    # totalDonations = Column(BigInteger)
    level = Column(Integer)

    def __init__(self,name,rockbiteID,level):
        self.name = name
        self.rockbiteID = rockbiteID
        self.level = level