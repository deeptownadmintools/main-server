from dtat.api.update import updateprint
from dtat.services.update import updateAll
from flask import jsonify


@updateprint.route('/all', methods=['GET', 'PATCH'])
def all():
    """
    Updates all guilds in database.
    """
    updateAll()
    return jsonify({'result': 'ok'})
