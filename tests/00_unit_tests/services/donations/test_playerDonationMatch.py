from dtat.services.donations.playerDonationMatch import playerDonationMatch
from datetime import datetime


class MockPlayer():
    def __init__(self, name):
        self.name = name


class MockCount():
    def __init__(self, player, donated, received):
        self.player = player
        self.donated = donated
        self.received = received


class MockTimeStamp():
    def __init__(self, counts, date):
        self.counts = counts
        self.date = date


def test_playerDonationMatch():
    p = MockPlayer('name')
    c = MockCount(p, 10, 20.8)
    now = datetime.utcnow()
    t = MockTimeStamp([c], now)

    res = playerDonationMatch(t)

    assert res == {
        'from': 'Dawn of time',
        'to': now,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': [
            [
                'name',
                10,
                20,
            ],
        ]
    }
