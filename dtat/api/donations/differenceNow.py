from dtat.api.donations import donationprint
from dtat.services.update import guildId
from dtat.models.timeStamp import TimeStamp
from dtat.services.donations import playerDonDiffMatch
from dtat.exceptions import DbException
from flask import jsonify


@donationprint.route('/difference/guild/id/<int:id1>/time/id/<int:id2>',
                     methods=['GET'])
def differenceNow(id1, id2):
    timeStamp1 = guildId(id1, True)['timeStamp']
    timeStamp2 = TimeStamp.query.get(id2)
    if timeStamp2 is None:
        raise DbException(404, 'Timestamp was not found.', ['timestamp_id'])
    return jsonify(playerDonDiffMatch(timeStamp1, timeStamp2))
