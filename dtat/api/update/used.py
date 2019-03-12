from dtat.api.update import updateprint
from dtat.services.update import updateUsed


@updateprint.route('/used', methods=['GET'])
def used():
    updateUsed()
    return 'ok'
