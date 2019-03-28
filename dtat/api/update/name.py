from dtat.api.update import updateprint
from dtat.services.update import guildName
from flask import jsonify


@updateprint.route('/name/<string:name>', methods=['GET'])
def name(name):
    """
    Updates database using Rockbite's api.
        :param name: guild name or its part
    """
    guildName(name)
    return jsonify({'result': 'ok'})
