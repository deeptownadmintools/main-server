from dtat.models import Guild
from datetime import datetime, timedelta
from dtat.services.update import guildObj


def updateUsed():
    """
    Updates every used guild's data in database
    """
    guilds = Guild.query.filter(
        Guild.lastVisited >= datetime.utcnow() - timedelta(365/12)).all()
    for a in guilds:
        guildObj(a)
