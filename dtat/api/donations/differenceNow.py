from dtat.api.donations import donationprint
from dtat.services.update import guildId
from dtat.models import TimeStamp
from dtat.services.donations import playerDonDiffMatch
from dtat.exceptions import DbException
from flask import jsonify


@donationprint.route('/difference/guild/id/<int:id1>/time/id/<int:id2>',
                     methods=['GET'])
def differenceNow(id1, id2):
    """
    Returns donations from given time up until now.
        :param id1: guild_id
        :param id2: timestamp_id
    """
    timeStamp2 = TimeStamp.query.get(id2)

    if timeStamp2 is None:
        raise DbException(404, 'Timestamp was not found.', ['timestamp_id'])

    if timeStamp2.guild_id != id1:
        raise DbException(400, 'Id mismatch', ['guild_id', 'timestamp_id'])

    timeStamp1 = guildId(id1, True, True)['timeStamp']

    return jsonify(playerDonDiffMatch(timeStamp1, timeStamp2))
