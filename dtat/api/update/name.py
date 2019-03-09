from dtat.api.update import update
from dtat.services.update import guildName
from flask import jsonify


@update.route('/name/<string:name>', methods=['GET'])
def name(name):
    return jsonify({"guild_ids": guildName(name)})
