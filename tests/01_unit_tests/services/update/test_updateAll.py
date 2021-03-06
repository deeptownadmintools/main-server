import mock
from dtat.services.update import updateAll


@mock.patch('dtat.services.update.guildObj')
@mock.patch('dtat.services.update.Guild')
def test_updateAll(mGld, mGldObj):
    mGld.query.all.return_value = [0, 1, 2, 3, 4, 5]
    updateAll()
    assert mGldObj.call_count == 6

    mGldObj.reset_mock()
    mGld.query.all.return_value = []
    updateAll()
    assert mGldObj.call_count == 0
