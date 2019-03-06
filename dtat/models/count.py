from dtat import app
from sqlalchemy import Column, Integer, BigInteger, ForeignKey


class Count(app.db.Model):
    __tablename__ = "count"
    timestamp_id = Column(Integer, ForeignKey("timestamp.id"))
    player_id = Column(Integer, ForeignKey("player.id"))
    donated = Column(BigInteger)
    received = Column(BigInteger)
