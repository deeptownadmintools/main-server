from dtat.api.update import updateprint
from dtat.services.update import updateAll


@updateprint.route('/all', methods=['GET'])
def all():
    updateAll()
    return 'ok'
