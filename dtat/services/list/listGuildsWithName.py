from dtat.models import Guild


def listGuildsWithName(name):
    """
    Returns list of guilds whose name contains with provided string
    (non case sensitive)
    :param name: start of guild name (non case sensitive)
    """
    return Guild.query.filter(Guild.name.like('%' + name + '%')).all()
