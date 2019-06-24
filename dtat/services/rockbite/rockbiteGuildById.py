from dtat import app
from dtat.exceptions import RockbiteException
import requests


def guildById(id):
    """
    Get guild data for a guild specified by guild's rockbite id.
        :param id: guild's rockbite id (str)
        :returns: json formated guild data
    """
    r = requests.get(
        app.config['ROCKBITE_URL']+id+"/donations",
        headers={'access_key': app.config['ROCKBITE_TOKEN']},
    ).json()

    if r['status'] != "ok":
        raise RockbiteException(
            404, "Api response was not ok.", [r['message']])

    return r
