from dtat.models import Guild
from dtat.services.update.update_guildObj import guildObj


def updateAll():
    """
    Updates every guild's data in database
    """
    guilds = Guild.query.all()
    for a in guilds:
        guildObj(a)
