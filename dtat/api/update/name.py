from dtat.api.update import updateprint
from dtat.services.update import guildName
from flask import jsonify


@updateprint.route('/name/<string:name>', methods=['GET'])
def name(name):
    guildName(name)
    return jsonify({'result': 'ok'})
