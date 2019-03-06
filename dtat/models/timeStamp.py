from dtat import app
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime


class TimeStamp(app.db.Model):
    __tablename__ = "timestamp"
    guild_id = Column(Integer, ForeignKey("guild.id"))
    counts = app.db.relationship('Count', backref='timestamp', lazy=True)
    date = Column(DateTime)
