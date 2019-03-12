from dtat.api.guild import guildprint
from dtat.services.list import guildWithId
from flask import jsonify
from dtat.models import Player


@guildprint.route('/id/<int:id>/data', methods=['GET'])
def data(id):
    guild = guildWithId(id)
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
