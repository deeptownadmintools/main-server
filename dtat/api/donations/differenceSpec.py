from dtat.api.donations import donationprint
from dtat.models.timeStamp import TimeStamp
from dtat.services.donations import playerDonDiffMatch
from dtat.exceptions import DbException
from flask import jsonify


@donationprint.route('/difference/time/id/<int:id1>/time/id/<int:id2>',
                     methods=['GET'])
def differenceSpec(id1, id2):
    timeStamp1 = TimeStamp.query.get(id1)
    timeStamp2 = TimeStamp.query.get(id2)
    if timeStamp1 is None or timeStamp2 is None:
        raise DbException(404, 'Timestamp was not found.', ['id'])
    return jsonify(playerDonDiffMatch(timeStamp1, timeStamp2))
