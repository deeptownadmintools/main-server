from dtat import app
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime


class TimeStamp(app.db.Model):
    __tablename__ = "timestamp"
    guild_id = Column(Integer, ForeignKey("guild.id"))
    counts = app.db.relationship('Count', backref='timestamp', lazy=True)
    date = Column(DateTime)

    def __init__(self, guild_id, date):
        self.guild_id = guild_id
        self.date = datetime.strptime(
            date,
            "%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def keys():
        return [
            'id',
            'date',
        ]

    def list(self):
        return [
            self.id,
            self.date,
        ]
