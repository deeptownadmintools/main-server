import mock
from dtat.models.player import Player
from dtat.models.guild import Guild
from datetime import datetime, timedelta


data1 = {
    "status": "ok",
    "result": [
        {
            "guild_id": "1",
            "guild_name": "Testtttttt",
            "level": 10
        },
        {
            "guild_id": "2",
            "guild_name": "testytesty",
            "level": 0
        },
        {
            "guild_id": "3",
            "guild_name": "test",
            "level": 0
        },
    ],
    "server_time": "2019-04-28T16:49:29.538Z"
}


data2 = {
    "status": "ok",
    "result": {
        "guild_id": "1",
        "guild_name": "Zion England",
        "guild_level": 16,
        "total_donations": 6284013.165,
        "total_level": 10453,
        "average_level": 209.06,
        "members": [
            {
                "user_id": "100333100473279671201",
                "user_name": "ChestnutSprite9338",
                "donations": 0,
                "last_online": "2019-04-17T22:51:08.064Z",
                "level": 69,
                "depth": 208,
                "smelters_count": 2,
                "crafters_count": 2,
                "miners_count": 13,
                "chemistry_mining_station_count": 4,
                "green_house_building_slot_count": 1,
                "chemistry_building_slot_count": 1
            },
            {
                "user_id": "100438959092138638847",
                "user_name": "raphaelbüchinger12",
                "donations": 236,
                "received_donation": 13,
                "last_event_donation": 0,
                "last_online": "2019-04-30T15:46:20.064Z",
                "level": 139,
                "depth": 387,
                "smelters_count": 2,
                "crafters_count": 2,
                "miners_count": 19,
                "chemistry_mining_station_count": 5,
                "green_house_building_slot_count": 1,
                "chemistry_building_slot_count": 2
            },
        ]
    }
}


@mock.patch('dtat.services.rockbite.rockbite_guildById.requests')
@mock.patch('dtat.services.rockbite.rockbite_guildByName.requests')
def test_updateId(mReqName, mReqId, client, app, session):
    assert len(Player.query.all()) == 0

    mReqId.get.return_value.json.return_value = data2
    res = client.get('/data/update/id/1')
    assert res.get_json()['message'] == 'Guild was not found'
    assert res.status_code == 404
    assert len(Player.query.all()) == 0


    mReqName.get.return_value.json.return_value = data1
    res = client.get('/data/update/name/test')


    data2['status'] = 'nok'
    mReqId.get.return_value.json.return_value = data2
    res = client.get('/data/update/id/1')
    assert res.status_code == 404
    assert res.get_json()['message'] == 'Api response was not ok.'


    data2['status'] = 'ok'
    mReqId.get.return_value.json.return_value = data2
    res = client.get('/data/update/id/1')
    assert res.get_json()['result'] == 'ok'
    assert res.status_code == 200
    assert len(Player.query.all()) == 2
