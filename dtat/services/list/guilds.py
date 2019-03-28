from dtat.models import Guild


def listGuilds():
    """
    Returns list of all guilds in database.
    """
    return Guild.query.all()
