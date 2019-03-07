from dtat import app
from dtat.exceptions import RockbiteException
from json import loads
import requests


def guildByName(name):
    r = loads(requests.get(
        app.config['ROCKBITE_URL']+"find",
        headers={'access_key': app.config['ROCKBITE_TOKEN']},
        params={'guild_name': name},
    ).text)

    if r['status'] != "ok":
        raise RockbiteException(404, "Api response was not ok.", ["status"])

    return r
