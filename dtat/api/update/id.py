from dtat.api.update import updateprint
from dtat.services.update import guildId


@updateprint.route('/id/<int:id>', methods=['GET'])
def id(id):
    guildId(id)
    return 'ok'
