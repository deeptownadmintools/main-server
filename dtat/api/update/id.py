from dtat.api.update import update
from dtat.services.update import guildId
from flask import jsonify


@update.route('/id/<int:id>', methods=['GET'])
def id(id):
    return jsonify({"player_ids": guildId(id)})
