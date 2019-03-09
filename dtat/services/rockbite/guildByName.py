from dtat import app
from dtat.exceptions import RockbiteException
import requests


def guildByName(name):
    """
    Get list of guilds with provided name.
        :param name: (part of) a guild name
        :returns: json formated list of guilds
    """
    r = requests.get(
        app.config['ROCKBITE_URL']+"find",
        headers={'access_key': app.config['ROCKBITE_TOKEN']},
        params={'guild_name': name},
    ).json

    if r['status'] != "ok":
        raise RockbiteException(404, "Api response was not ok.", ["status"])

    return r
