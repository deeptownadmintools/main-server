import mock
import pytest
# import sys
# sys.modules['dtat.services.update.guildObj.guildObj'] = mock.MagicMock()
# sys.modules['dtat.services.update.guildObj'] = mock.MagicMock()
# sys.modules['guildObj'] = mock.MagicMock()
# from dtat.services.update.guildObj import guildObj
from dtat.services.update.update_guildId import guildId
from dtat.exceptions.dbException import DbException


class MockQuery():
    def get(i=1):
        if i == 1:
            return 'ok'
        return None


class MockGuild():
    def __init__(self):
        self.query = MockQuery()


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
