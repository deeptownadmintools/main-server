from dtat.api.update import update
from dtat.services.update import updateUsed


@update.route('/used', methods=['GET'])
def used():
    updateUsed()
    return 'ok'
