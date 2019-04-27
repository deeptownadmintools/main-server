import mock
import pytest
from dtat.services.rockbite.guildByName import guildByName
from dtat.exceptions.rockbiteException import RockbiteException


class MockObj():
    def json():
        return{'status': 'ok'}


@mock.patch('dtat.app')
@mock.patch('requests.get', return_value=MockObj)
def test_guildById_ok(mApp, mReq):
    r = guildByName('1')
    assert r == {'status': 'ok'}


class MockObj2():
    def json():
        return{'status': 'nok'}


@mock.patch('dtat.app')
@mock.patch('requests.get', return_value=MockObj2)
def test_guildById_nok(mApp, mReq):
    with pytest.raises(RockbiteException):
        r = guildByName('1')
        assert False