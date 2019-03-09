from dtat.api.update import updateprint
from dtat.services.update import updateUsed


@update.route('/used', methods=['GET'])
def used():
    updateUsed()
    return 'ok'
