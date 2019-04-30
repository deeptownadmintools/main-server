from dtat.services.donations.playerDonDiffMatch import playerDonDiffMatch
from datetime import datetime, timedelta


class MockPlayer():
    def __init__(self, name):
        self.name = name


class MockCount():
    def __init__(self, player, donated, received, player_id):
        self.player = player
        self.donated = donated
        self.received = received
        self.player_id = player_id


class MockTimeStamp():
    def __init__(self, id, counts, date):
        self.id = id
        self.counts = counts
        self.date = date


def test_playerDonDiffMatch():
    p1 = MockPlayer('name1')
    p2 = MockPlayer('name2')
    p3 = MockPlayer('name3')
    c1 = MockCount(p1, 10, 20.8, 1)
    c2 = MockCount(p1, 20, 30.8, 1)
    c3 = MockCount(p2, 20, 30.8, 2)
    c4 = MockCount(p3, 20, 30.8, 3)
    now = datetime.utcnow()
    before = now - timedelta(days=1)
    t1 = MockTimeStamp(1, [c1, c3], before)
    t2 = MockTimeStamp(2, [c2, c4], now)

    res1 = playerDonDiffMatch(t1, t2)

    assert res1 == {
        'from': before,
        'to': now,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': [
            [
                'name1',
                10,
                10,
            ],
            [
                'name2',
                '/',
                '/',
            ],
        ]
    }

    res2 = playerDonDiffMatch(t2, t1)

    assert res2 == {
        'from': before,
        'to': now,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': [
            [
                'name1',
                10,
                10,
            ],
            [
                'name2',
                '/',
                '/',
            ],
        ]
    }

    res3 = playerDonDiffMatch(t1, t1)

    assert res3 == {
        'from': before,
        'to': before,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': [
            [
                'name1',
                0,
                0,
            ],
            [
                'name2',
                0,
                0,
            ],
        ]
    }
