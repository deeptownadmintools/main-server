from flask import Blueprint
from dtat.services.dataProcessing import guildName, guildId
from dtat.services.rockbite import guildByName


homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    return "DeepTownAdminTools - main server"

@homeprint.route('/test')
def test():

    guildId(11,"591baa171dc27b0c828e524e")
    return "ok"