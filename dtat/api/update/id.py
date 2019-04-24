from dtat.api.update import updateprint
from dtat.services.update import guildId
from flask import jsonify


@updateprint.route('/id/<int:id>', methods=['GET', 'PATCH'])
def id(id):
    """
    Updates one guild specified by guild id.
        :param id: guild_id
    """
    guildId(id)
    return jsonify({'result': 'ok'})
