from dtat.services.update.guildObj import guildObj
from dtat.models import Guild
from dtat.exceptions import DbException


def guildId(id, respond=False):
    """
    Updates guild data in database
        :param id: database id of a guild
        :param respond: nothing will be returned if False
        :returns: {
            'players': [...],
            'guild': obj,
            'timeStamp': obj
        }
        :raises DBException: DBException is raised, when guild with specified id was not found. # noqa: E501
    """
    guild = Guild.query.get(id)
    if guild is None:
        raise DbException(404, "Guild was not found", ["id"])
    return guildObj(guild, respond)
