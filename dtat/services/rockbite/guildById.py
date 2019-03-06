from dtat import app
from dtat.exceptions import RockbiteException
from json import loads
import requests


def guildById(id):
    r = loads(requests.get(
        app.config['ROCKBITE_URL']+id+"/donations",
        headers={'access_key': app.config['ROCKBITE_TOKEN']},
    ).text)

    if r['status'] != "ok":
        raise RockbiteException(404,"Api response was not ok.", ["status"])
    
    return r

