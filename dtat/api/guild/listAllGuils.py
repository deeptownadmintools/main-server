from dtat.api.guild import guildprint
from dtat.services.list import listGuilds
from flask import jsonify
from dtat.models import Guild


@guildprint.route('/all', methods=['GET'])
def listAllGuils():
    guilds = listGuilds()
    data = []
    for a in guilds:
        data.append(a.list())

    return jsonify({
        'keys': Guild.keys(),
        'data': data
    })
