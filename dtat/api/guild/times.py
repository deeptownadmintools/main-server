from dtat.api.guild import guildprint
from dtat.services.list import guildWithId
from flask import jsonify
from dtat.models import TimeStamp


@guildprint.route('/id/<int:id>/times', methods=['GET'])
def times(id):
    """
    Returns list of timestamps.
        :param id: guild_id
    """
    guild = guildWithId(id)
    data = []
    for a in guild.timeStamps:
        data.append(a.list())

    return jsonify({
        'id': guild.id,
        'name': guild.name,
        'times': {
            'keys': TimeStamp.keys(),
            'data': data
        }
    })
