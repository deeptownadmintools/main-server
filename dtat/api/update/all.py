from dtat.api.update import update
from dtat.services.update import updateAll


@update.route('/all', methods=['GET'])
def all():
    updateAll()
    return 'ok'
