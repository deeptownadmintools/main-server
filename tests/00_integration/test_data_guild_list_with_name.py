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


@mock.patch('dtat.services.rockbite.rockbite_guildById.requests')
@mock.patch('dtat.services.rockbite.rockbite_guildByName.requests')
def test_guildListWithName(mReqName, mReqId, client, app, session):
    mReqName.get.return_value.json.return_value = data1

    res = client.get('/data/guild/name/test')
    assert res.status_code == 200
    assert res.get_json()['keys'] == [
        'id',
        'name',
        'level',
    ]
    assert res.get_json()['data'] == [
        [1, 'Testtttttt', 10],
        [2, 'testytesty', 0],
        [3, 'test', 0],
    ]

    res = client.get('/data/guild/name/testy')
    assert res.status_code == 200
    assert res.get_json()['keys'] == [
        'id',
        'name',
        'level',
    ]
    assert res.get_json()['data'] == [
        [2, 'testytesty', 0],
    ]
