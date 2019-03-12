from dtat.models import Guild


def listGuilds():
    return Guild.query.all()
