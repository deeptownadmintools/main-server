from flask import Blueprint

homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    return "DeepTownAdminTools - main server"
