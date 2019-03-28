from dtat.models import Guild
from datetime import datetime
from dtat import app
from dtat.exceptions import DbException


def guildWithId(guildId):
    """
    Returns guild with given id.
        :param guildId: guild_id
        :returns: instance of Guild object
    """
    guild = Guild.query.get(guildId)
    if guild is None:
        raise DbException(404, "Guild was not found.", ['id'])

    guild.lastVisited = datetime.utcnow()
    app.db.session.commit()
    return guild
