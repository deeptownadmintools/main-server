from flask import Blueprint, jsonify


homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    """
    Api method for testing purposes.
    """
    return "DeepTownAdminTools - main server"


@homeprint.route('/test')
def test():
    """
    Api method for testing purposes.
    """
    data = []
    for a in range(10000):
        data.append(
            [
                123456789,
                '1234567890123456789012345678901234567890',
                123,
            ]
        )

    return jsonify({
        'keys': [
            'id',
            'name',
            'level',
        ],
        'data': data
    })
