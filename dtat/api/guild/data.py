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
        try:
            guild = guildObj(guild, True, True)['guild']
        except DTATException as e:
            if e.invalid == ["Invalid guild id"]:
                removeGuild(guild)
                raise DTATException(410, "Guild has been deleted.", ["guild"])
            else:
                raise DTATException(e.errorCode, e.message, e.invalid)

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
