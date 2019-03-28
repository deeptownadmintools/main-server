from dtat.api.donations import donationprint
from dtat.services.update import guildId
from dtat.services.donations import playerDonationMatch
from flask import jsonify


@donationprint.route('/current/guild/id/<int:id>', methods=['GET'])
def current(id):
    """
    Returns donations from dawn of time up until now.
        :param id: guild_id
    """
    data = guildId(id, True, True)
    return jsonify(playerDonationMatch(data['timeStamp']))
