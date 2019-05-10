import mock


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


nok = {
    "status": "nok",
    "message": "Invalid guild id",
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


@mock.patch('dtat.services.rockbite.rockbite_guildById.requests')
@mock.patch('dtat.services.rockbite.rockbite_guildByName.requests')
def test_guildData(mReqName, mReqId, client, app, session):
    mReqName.get.return_value.json.return_value = data1
    mReqId.get.return_value.json.return_value = nok

    client.get('/data/update/name/test')

    res = client.get('/data/guild/id/3/data')
    assert res.status_code == 410
    assert res.get_json()['message'] == 'Guild has been deleted.'

    mReqId.get.return_value.json.return_value = data2
    res = client.get('/data/guild/id/3/data')
    assert res.status_code == 404
    assert res.get_json()['message'] == 'Guild was not found.'

    res = client.get('/data/guild/id/1/data')
    assert res.status_code == 200
    assert res.get_json()['id'] == 1
    assert res.get_json()['name'] == "Zion England"
    assert res.get_json()['level'] == 16
    assert res.get_json()['players']['keys'] == [
        'id',
        'name',
        'lastOnline',
        'level',
        'depth',
        'mine',
        'chemMine',
        'oil',
        'crafters',
        'smelters',
        'jewel',
        'chemStation',
        'greenHouse',
        'lastEventDonation',
    ]
    assert res.get_json()['players']['data'] == [
        [1, 'a', 'Wed, 17 Apr 2019 22:51:08 GMT',
            69, 208, 13, 4, 0, 2, 2, 0, 1, 1, 0],
        [2, 'b', 'Tue, 30 Apr 2019 15:46:20 GMT',
            139, 387, 19, 5, 0, 2, 2, 0, 2, 1, 0],
    ]
