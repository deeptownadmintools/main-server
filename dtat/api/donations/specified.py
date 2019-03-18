from dtat.api.donations import donationprint
from dtat.models.timeStamp import TimeStamp
from dtat.services.donations import playerDonationMatch
from dtat.exceptions import DbException
from flask import jsonify
from dtat import app
from datetime import datetime


@donationprint.route('/specified/time/id/<int:id>', methods=['GET'])
def specified(id):
    data = TimeStamp.query.get(id)
    if data is None:
        raise DbException(404, 'Timestamp was not found.', ['id'])
    data.guild.lastVisited = datetime.utcnow()
    app.db.session.commit()
    return jsonify(playerDonationMatch(data))
