import mock
from dtat.models.count import Count


@mock.patch('dtat.app', new_callable=object)
def test_count(mApp):

    c = Count(1, 2, 3, 4)
    assert c.timestamp_id == 1
    assert c.player_id == 2
    assert c.donated == 3
    assert c.received == 4
