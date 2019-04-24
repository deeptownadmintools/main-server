from dtat.api.update import updateprint
from dtat.services.update import updateUsed
from flask import jsonify


@updateprint.route('/used', methods=['GET', 'PATCH'])
def used():
    """
    Updates all used guilds.
    """
    updateUsed()
    return jsonify({'result': 'ok'})
