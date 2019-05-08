import mock
from dtat.models.guild import Guild


data = {
    "status": "nok",
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


@mock.patch('dtat.services.rockbite.rockbite_guildByName.requests')
def test_updateName(mReq, client, app, session):
    assert len(Guild.query.all()) == 0

    mReq.get.return_value.json.return_value = data
    res = client.get('/data/update/name/test')
    assert res.status_code == 404
    assert res.get_json()['message'] == 'Api response was not ok.'
    assert len(Guild.query.all()) == 0

    data['status'] = 'ok'
    mReq.get.return_value.json.return_value = data
    res = client.get('/data/update/name/test')
    assert res.get_json()['result'] == 'ok'
    assert res.status_code == 200
    assert len(Guild.query.all()) == 3

    data['status'] = 'nok'
    mReq.get.return_value.json.return_value = data
    res = client.get('/data/update/name/test')
    assert res.status_code == 404
    assert res.get_json()['message'] == 'Api response was not ok.'
    assert len(Guild.query.all()) == 3

    data['status'] = 'ok'
    data["result"] = [
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
        {
            "guild_id": "4",
            "guild_name": "test",
            "level": 0
        },
    ]
    mReq.get.return_value.json.return_value = data
    res = client.get('/data/update/name/test')
    assert res.get_json()['result'] == 'ok'
    assert res.status_code == 200
    assert len(Guild.query.all()) == 4
