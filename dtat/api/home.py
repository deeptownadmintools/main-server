from flask import Blueprint
from dtat.services.update import guildId


homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    return "DeepTownAdminTools - main server"


@homeprint.route('/test')
def test():
    """
    Api method soleley for testing purposes
    """
    guildId(11, "591baa171dc27b0c828e524e")
    return "ok"
