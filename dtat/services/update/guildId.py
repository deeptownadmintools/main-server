from dtat.services.update.guildObj import guildObj
from dtat.models import Guild
from dtat.exceptions import DbException


def guildId(id):
    """
    Updates guild data in database
        :param id: database id of a guild
        :returns: list of ids of players whose data had been updated
        :raises DBException: DBException is raised if player with specified id was not found
    """
    guild = Guild.query.get(id)
    if guild is None:
        raise DbException(404, "Guild was not found", ["id"])
    return guildObj(guild)
