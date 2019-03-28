from dtat.api.guild import guildprint
from dtat.services.list import guildWithId
from dtat.services.update import guildObj
from flask import jsonify
from dtat.models import Player
from dtat.services.remove import removeGuild
from dtat.exceptions import DTATException


@guildprint.route('/id/<int:id>/data', methods=['GET'])
def data(id):
    """
    Returns guild data.
        :param id: guild_id
    """
    guild = guildWithId(id)
    if len(guild.players) == 0:
        guild = guildObj(guild, True, True)['guild']
        if len(guild.players) == 0:
            removeGuild(guild)
            raise DTATException(410, "Guild has been deleted.", ["guild"])

    data = []
    for a in guild.players:
        data.append(a.list())

    return jsonify({
        'id': guild.id,
        'name': guild.name,
        'level': guild.level,
        'players': {
            'keys': Player.keys(),
            'data': data
        }
    })
