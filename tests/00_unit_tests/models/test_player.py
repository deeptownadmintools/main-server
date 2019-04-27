import mock
from dtat.models.player import Player
from datetime import datetime


@mock.patch('dtat.app', new_callable=object)
@mock.patch('dtat.app.db.relationship', new_callable=None)
def test_player_partial(mApp, mRel):
    p = Player(1, 2, 3, None)

    assert p.guild_id == 1
    assert p.name == 2
    assert p.rockbiteId == 3
    assert p.lastOnline == None
    assert p.level == None
    assert p.depth == None
    assert p.mine == None
    assert p.chemMine == None
    assert p.oil == None
    assert p.crafters == None
    assert p.smelters == None
    assert p.jewel == None
    assert p.chemStation == None
    assert p.greenHouse == None
    assert p.lastEventDonation == None

    assert p.keys() == [
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
    assert Player.keys() == [
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
    p.id = 1
    assert p.list() == [
        1,
        2,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]


@mock.patch('dtat.app', new_callable=object)
@mock.patch('dtat.app.db.relationship', new_callable=None)
def test_player_full(mApp, mRel):
    p = Player(1, 2, 3, None)

    assert p.guild_id == 1
    assert p.name == 2
    assert p.rockbiteId == 3

    p = Player(1, 2, 3, '2019-04-25T16:51:10.228Z',
               5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    date = datetime.strptime(
        '2019-04-25T16:51:10.228Z',
        "%Y-%m-%dT%H:%M:%S.%fZ")

    assert p.guild_id == 1
    assert p.name == 2
    assert p.rockbiteId == 3
    assert p.lastOnline == date
    assert p.level == 5
    assert p.depth == 6
    assert p.mine == 7
    assert p.chemMine == 8
    assert p.oil == 9
    assert p.crafters == 10
    assert p.smelters == 11
    assert p.jewel == 12
    assert p.chemStation == 13
    assert p.greenHouse == 14
    assert p.lastEventDonation == 15

    assert p.keys() == [
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
    assert Player.keys() == [
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
    p.id = 1
    assert p.list() == [
        1,
        2,
        date,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]
