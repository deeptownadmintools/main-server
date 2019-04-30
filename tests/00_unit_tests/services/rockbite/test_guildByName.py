import mock
import pytest
from dtat.services.rockbite.rockbite_guildByName import guildByName
from dtat.exceptions.rockbiteException import RockbiteException


@mock.patch('dtat.app')
@mock.patch('requests.get')
def test_guildById_ok(mReq, mApp):
    mReq.return_value.json.return_value = {'status': 'ok'}
    r = guildByName('1')
    assert r == {'status': 'ok'}


@mock.patch('dtat.app')
@mock.patch('requests.get')
def test_guildById_nok(mReq, mApp):
    mReq.return_value.json.return_value = {'status': 'nok'}
    with pytest.raises(RockbiteException):
        r = guildByName('1')
        assert False