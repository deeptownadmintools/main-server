from flask import Blueprint
from dtat.exceptions import DTATException
from flask import jsonify


donationprint = Blueprint('donations', __name__, url_prefix='/donations')


from dtat.api.donations.current import current  # noqa F402
from dtat.api.donations.specified import specified  # noqa F402
from dtat.api.donations.differenceNow import differenceNow  # noqa F402
from dtat.api.donations.differenceSpec import differenceSpec  # noqa F402


@donationprint.errorhandler(DTATException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'donationprint',
    'current',
    'specified',
    'differenceNow',
    'differenceSpec',
]
