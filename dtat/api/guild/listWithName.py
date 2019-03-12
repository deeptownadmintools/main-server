from dtat.api.guild import guildprint
from dtat.services.list import listGuildsWithName
from flask import jsonify
from dtat.models import Guild


@guildprint.route('/name/<string:name>', methods=['GET'])
def listWithName(name):
    guilds = listGuildsWithName(name)
    data = []
    for a in guilds:
        data.append(a.list())

    return jsonify({
        'keys': Guild.keys(),
        'data': data
    })
