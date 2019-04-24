from flask import Blueprint
from dtat.exceptions import DTATException
from flask import jsonify


guildprint = Blueprint('guild', __name__, url_prefix='/data/guild')


from dtat.api.guild.listAllGuils import listAllGuils  # noqa F402
from dtat.api.guild.listWithName import listWithName  # noqa F402
from dtat.api.guild.data import data  # noqa F402
from dtat.api.guild.times import times  # noqa F402


@guildprint.errorhandler(DTATException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'guildprint',
    'listAllGuils',
    'listWithName',
    'data',
    'times',
]
