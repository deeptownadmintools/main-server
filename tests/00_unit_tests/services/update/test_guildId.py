import mock
import pytest
from dtat.services.update.update_guildId import guildId
from dtat.exceptions.dbException import DbException


@mock.patch('dtat.models.Guild.query')
@mock.patch('dtat.services.update.update_guildId.guildObj')
def test_guildId_nok(mGObj, mQ):
    mQ.get.return_value = None
    with pytest.raises(DbException):
        guildId(1)
        assert False


@mock.patch('dtat.models.Guild.query')
@mock.patch('dtat.services.update.update_guildId.guildObj', return_value='ok')
def test_guildId_ok(mGObj, mQ):
    mQ.get.return_value = 'ok'
    assert guildId(1) == 'ok'
    mGObj.assert_called_once()
    mGObj.assert_called_with('ok', False, False)
    mGObj.reset_mock()
    assert guildId(1,True, True) == 'ok'
    mGObj.assert_called_once()
    mGObj.assert_called_with('ok', True, True)
