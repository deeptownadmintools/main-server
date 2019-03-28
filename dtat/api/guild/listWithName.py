from dtat.api.guild import guildprint
from dtat.services.list import listGuildsWithName
from flask import jsonify
from dtat.models import Guild
from dtat.services.update import guildName


@guildprint.route('/name/<string:name>', methods=['GET'])
def listWithName(name):
    """
    Returns list of guilds matching given name.
        :param name: start of a guild (non case sensitive)
    """
    guilds = listGuildsWithName(name)
    if len(guilds) == 0:
        guildName(name)
        guilds = listGuildsWithName(name)
    data = []
    for a in guilds:
        data.append(a.list())

    return jsonify({
        'keys': Guild.keys(),
        'data': data
    })
