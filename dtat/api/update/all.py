from dtat.api.update import updateprint
from dtat.services.update import updateAll
from flask import jsonify


@updateprint.route('/all', methods=['GET'])
def all():
    updateAll()
    return jsonify({'result': 'ok'})
