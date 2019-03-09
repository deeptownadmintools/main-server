from dtat.models import Guild
from dtat.services.update import guildObj


def updateAll():
    """
    Updates every guild's data in database
    """
    guilds = Guild.query.all()
    for a in guilds:
        guildObj(a)
