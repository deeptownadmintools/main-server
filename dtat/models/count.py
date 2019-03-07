from dtat import app
from sqlalchemy import Column, Integer, BigInteger, ForeignKey


class Count(app.db.Model):
    __tablename__ = "count"
    timestamp_id = Column(Integer, ForeignKey("timestamp.id"))
    player_id = Column(Integer, ForeignKey("player.id"))
    donated = Column(BigInteger)
    received = Column(BigInteger)

    def __init__(self, timestamp_id, player_id, donated, received):
        self.timestamp_id = timestamp_id
        self.player_id = player_id
        self.donated = donated
        self.received = received
