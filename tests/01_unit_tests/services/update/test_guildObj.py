import mock
from datetime import datetime, timedelta
from dtat.services.update import guildObj


data = {
    'result': {
        "guild_id": "idG",
        "guild_name": "gName",
        "guild_level": 1,
        "members": [
            {
                "user_id": "idU",
                "user_name": "nameU",
                "donations": 0,
                "last_online": "2019-04-17T22:51:08.064Z",
                "level": 1,
                "depth": 2,
                "smelters_count": 3,
                "crafters_count": 4,
                "miners_count": 5,
                "chemistry_mining_station_count": 6,
                "green_house_building_slot_count": 7,
                "chemistry_building_slot_count": 8
            },
        ]
    }
}


class MockGuild():
    def __init__(self, name, idR, lvl, players):
        self.id = str(name) + str(idR) + str(lvl)
        self.name = name
        self.rockbiteId = idR
        self.lvl = lvl
        self.players = players


class MockTimeStamp():
    def __init__(self, gldId, date):
        self.id = str(gldId) + str(date)
        self.guild_id = gldId
        self.date = date
        self.counts = []


class MockCount():
    def __init__(self, tId, pId, don, rec):
        self.id = str(tId) + str(pId)
        self.timeStamp_id = tId
        self.player_id = pId
        self.don = don
        self.rec = rec


class MockPlayer():
    def __init__(self, guild_id, name, idR, lastOnline, lvl=0, depth=0,
                 mine=0, chem=0, oil=0, craft=0, smelt=0, jewel=0, chemSt=0,
                 green=0, lastEvDon=0):
        self.id = str(guild_id) + str(name) + str(idR)
        self.guild_id = guild_id
        self.name = name
        self.rockbiteId = idR
        self.lastOnline = lastOnline
        self.level = lvl
        self.depth = depth
        self.mine = mine
        self.chemMine = chem
        self.oil = oil
        self.crafters = craft
        self.smelters = smelt
        self.jewel = jewel
        self.chemStation = chemSt
        self.greenHouse = green
        self.lastEventDonation = lastEvDon


@mock.patch('dtat.services.update.datetime',
            return_value=datetime.utcnow())
@mock.patch('dtat.services.update.app')
@mock.patch('dtat.services.update.Player',
            side_effect=MockPlayer)
@mock.patch('dtat.services.update.Count',
            side_effect=MockCount)
@mock.patch('dtat.services.update.TimeStamp',
            side_effect=MockTimeStamp)
@mock.patch('dtat.services.update.guildById',
            return_value=data)
def test_guildObj(mGldById, mTS, mC, mP, mApp, mDate):
    mTS.query.filter_by.return_value\
        .order_by.return_value\
        .first.return_value = None
    mP.query.filter_by.return_value\
        .first.return_value = None
    now = datetime.utcnow()
    p = MockPlayer(1, '1', '1', now)
    mP.query.filter_by.return_value\
        .all.return_value = [p]
    mDate.utcnow.return_value = now

    g = MockGuild('g', 'idG', 1, [p])
    assert guildObj(g) is None
    assert mDate.utcnow.call_count == 1

    mDate.reset_mock()
    assert guildObj(g, False, False) is None
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, False)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, True)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 2

    mApp.reset_mock()
    mDate.reset_mock()
    assert guildObj(g, False, True) is None
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert mDate.utcnow.call_count == 2

    ts = MockTimeStamp(g.id, now-timedelta(minutes=20))
    mTS.query.filter_by.return_value\
        .order_by.return_value\
        .first.return_value = ts

    mDate.reset_mock()
    assert guildObj(g, False, False) is None
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, False)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, True)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 2

    mApp.reset_mock()
    mDate.reset_mock()
    assert guildObj(g, False, True) is None
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert mDate.utcnow.call_count == 2

    ts = MockTimeStamp(g.id, now-timedelta(minutes=20))
    mTS.query.filter_by.return_value\
        .order_by.return_value\
        .first.return_value = ts

    mDate.reset_mock()
    assert guildObj(g, False, False) is None
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, False)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 1

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, True)
    assert res['players'][0].id == '111'
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(now)
    assert mDate.utcnow.call_count == 2

    mApp.reset_mock()
    mDate.reset_mock()
    assert guildObj(g, False, True) is None
    args, kwargs = mApp.db.session.add.call_args_list[1]
    assert args[0].id == 'gidG1nameUidU'
    assert mDate.utcnow.call_count == 2

    ts = MockTimeStamp(g.id, now-timedelta(minutes=5))
    mTS.query.filter_by.return_value\
        .order_by.return_value\
        .first.return_value = ts

    mDate.reset_mock()
    mApp.reset_mock()
    assert guildObj(g, False, False) is None
    assert mDate.utcnow.call_count == 1
    assert mApp.db.session.add.call_count == 0

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, False)
    assert res['players'][0].id == '111'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(ts.date)
    assert mDate.utcnow.call_count == 1
    assert mApp.db.session.add.call_count == 0

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, True)
    assert res['players'][0].id == '111'
    assert res['guild'].id == 'gidG1'
    assert res['timeStamp'].id == 'gidG1'+str(ts.date)
    assert mDate.utcnow.call_count == 1
    assert mApp.db.session.add.call_count == 0

    mApp.reset_mock()
    mDate.reset_mock()
    assert guildObj(g, False, True) is None
    assert mDate.utcnow.call_count == 1
    assert mApp.db.session.add.call_count == 0

    mGldById.return_value = {
        'result': {
            "guild_id": "idG",
            "guild_name": "gName",
            "guild_level": 1,
            "members": []
        }
    }
    mTS.query.filter_by.return_value\
        .order_by.return_value\
        .first.return_value = None

    mApp.reset_mock()
    mDate.reset_mock()
    res = guildObj(g, True, True)
    assert res['players'][0].guild_id is None
    assert res['players'][0].id == '111'
    assert mDate.utcnow.call_count == 2
    assert mApp.db.session.add.call_count == 1
