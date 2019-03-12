from dtat.models import Guild


def listGuildsWithName(name):
    return Guild.query.filter(Guild.name.like(name + '%')).all()
