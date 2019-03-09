from flask import Blueprint
from dtat.exceptions import DTATException
from flask import jsonify

update = Blueprint('update', __name__, url_prefix='/update')


from dtat.api.update.id import id  # noqa F402
from dtat.api.update.name import name  # noqa F402
from dtat.api.update.all import all  # noqa F402
from dtat.api.update.used import used  # noqa F402


@update.errorhandler(DTATException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'update',
    'id',
    'name',
    'all',
    'used',
    '__response_err',
]
