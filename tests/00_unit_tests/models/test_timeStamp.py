import mock
from dtat.models.timeStamp import TimeStamp


@mock.patch('dtat.app.db.Model', new_callable=object)
@mock.patch('dtat.app.db.relationship', return_value=None)
def test_timeStamp(mModel, mApp):
    t = TimeStamp(1, 2)
    assert t.guild_id == 1
    assert t.date == 2
    assert t.keys() == [
        'id',
        'date',
    ]
    assert TimeStamp.keys() == [
        'id',
        'date',
    ]
    t.id = 1
    assert t.list() == [
        1,
        2,
    ]
