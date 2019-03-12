from dtat.api.update import updateprint
from dtat.services.update import guildName


@updateprint.route('/name/<string:name>', methods=['GET'])
def name(name):
    guildName(name)
    return 'ok'
