import mock
from dtat.models.player import Player
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
        "guild_name": "Testtttttt",
        "guild_level": 16,
        "members": [
            {
                "user_id": "1",
                "user_name": "ChestnutSprite9338",
                "donations": 0,
                "last_online": "2019-04-17T22:51:08.064Z",
                "level": 2,
                "depth": 208,
                "smelters_count": 2,
                "crafters_count": 2,
                "miners_count": 13,
                "chemistry_mining_station_count": 4,
                "green_house_building_slot_count": 1,
                "chemistry_building_slot_count": 1
            },
            {
                "user_id": "2",
                "user_name": "raphaelbüchinger12",
                "donations": 236,
                "received_donation": 13,
                "last_event_donation": 0,
                "last_online": "2019-04-30T15:46:20.064Z",
                "level": 2,
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


data3 = {
    "status": "ok",
    "result": {
        "guild_id": "2",
        "guild_name": "testytesty",
        "guild_level": 16,
        "members": [
            {
                "user_id": "3",
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
                "user_id": "4",
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


data4 = {
    "status": "ok",
    "result": {
        "guild_id": "3",
        "guild_name": "testytesty",
        "guild_level": 16,
        "members": [
            {
                "user_id": "5",
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
                "user_id": "6",
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


data5 = {
    "status": "ok",
    "result": {
        "guild_id": "1",
        "guild_name": "Testtttttt",
        "guild_level": 16,
        "members": [
            {
                "user_id": "1",
                "user_name": "ChestnutSprite9338",
                "donations": 0,
                "last_online": "2019-04-17T22:51:08.064Z",
                "level": 1,
                "depth": 208,
                "smelters_count": 2,
                "crafters_count": 2,
                "miners_count": 13,
                "chemistry_mining_station_count": 4,
                "green_house_building_slot_count": 1,
                "chemistry_building_slot_count": 1
            },
            {
                "user_id": "2",
                "user_name": "raphaelbüchinger12",
                "donations": 236,
                "received_donation": 13,
                "last_event_donation": 0,
                "last_online": "2019-04-30T15:46:20.064Z",
                "level": 1,
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
@mock.patch('dtat.services.update.update_guildObj.datetime')
def test_updateUsed(mDate, mReqName, mReqId, client, app, session):
    mReqId.get.return_value.json.return_value = data5
    assert len(Player.query.all()) == 0

    mDate.utcnow.return_value = datetime.utcnow() - timedelta(1)
    mDate.strptime.return_value = datetime.utcnow() - timedelta(1)

    mReqName.get.return_value.json.return_value = data1
    client.get('/data/update/name/test')
    assert len(Player.query.all()) == 0

    mReqId.get.return_value.json.return_value = data5
    client.get('/data/guild/id/1/data')
    assert len(Player.query.all()) == 2

    for i in Player.query.all():
        assert i.level == 1

    mDate.utcnow.return_value = datetime.utcnow()
    mReqId.get.return_value.json.side_effect = [data2, data3, data4]
    client.get('/data/update/used')
    assert len(Player.query.all()) == 2

    for i in Player.query.all():
        assert i.level == 2
