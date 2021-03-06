import mock
from datetime import datetime


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
        "guild_name": "Testtttttt",
        "guild_level": 16,
        "total_donations": 6284013.165,
        "total_level": 10453,
        "average_level": 209.06,
        "members": [
            {
                "user_id": "100333100473279671201",
                "user_name": "a",
                "donations": 30,
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
                "user_name": "b",
                "donations": 20,
                "received_donation": 10,
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


@mock.patch('dtat.services.rockbite.rockbiteGuildById.requests')
@mock.patch('dtat.services.rockbite.rockbiteGuildByName.requests')
@mock.patch('dtat.services.update.datetime')
def test_guildListTimes(mDate, mReqName, mReqId, client, app, session):
    mReqName.get.return_value.json.return_value = data1
    mReqId.get.return_value.json.return_value = data2

    mDate.utcnow.return_value = datetime(2019, 5, 10, 1, 1, 1, 1)
    mDate.strptime.return_value = datetime(2019, 5, 10, 1, 1, 1, 1)

    res = client.get('/data/guild/id/1/times')
    assert res.status_code == 404
    assert res.get_json()['message'] == 'Guild was not found.'

    client.get('/data/update/name/test')

    res = client.get('/data/guild/id/1/times')
    assert res.status_code == 200
    assert res.get_json()['id'] == 1
    assert res.get_json()['name'] == "Testtttttt"
    assert res.get_json()['times']['keys'] == [
        'id',
        'date',
    ]
    assert res.get_json()['times']['data'] == []

    client.get('/data/update/id/1')

    res = client.get('/data/guild/id/1/times')
    assert res.status_code == 200
    assert res.get_json()['id'] == 1
    assert res.get_json()['name'] == "Testtttttt"
    assert res.get_json()['times']['keys'] == [
        'id',
        'date',
    ]
    assert res.get_json()['times']['data'][0][0] == 1
    assert res.get_json()[
        'times']['data'][0][1] == 'Fri, 10 May 2019 01:01:01 GMT'
