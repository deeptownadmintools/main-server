from dtat.api.update import updateprint
from dtat.services.update import guildId
from flask import jsonify


@updateprint.route('/id/<int:id>', methods=['GET'])
def id(id):
    guildId(id)
    return jsonify({'result': 'ok'})
