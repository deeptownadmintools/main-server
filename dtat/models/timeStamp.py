from dtat import app
from sqlalchemy import Column, Integer, ForeignKey, DateTime


class TimeStamp(app.db.Model):
    """
    Database model for each donation time.
    """
    __tablename__ = "timestamp"
    guild_id = Column(Integer, ForeignKey("guild.id"))
    counts = app.db.relationship('Count', backref='timestamp', lazy=True)
    date = Column(DateTime)

    def __init__(self, guild_id, date):
        self.guild_id = guild_id
        self.date = date

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
