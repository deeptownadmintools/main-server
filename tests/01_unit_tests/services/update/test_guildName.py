import mock
from dtat.services.update import guildName


data = {
    'result': [
        {
            "guild_id": "string1",
            "guild_name": "name1",
            "level": 1
        }
    ]
}


class MockGuild():
    def __init__(self, name, idR, lvl):
        self.id = str(name) + str(idR) + str(lvl)
        self.name = name
        self.idR = idR
        self.lvl = lvl


@mock.patch('dtat.services.update.guildByName',
            return_value=data)
@mock.patch('dtat.services.update.app')
@mock.patch('dtat.services.update.app.db.session')
@mock.patch('dtat.services.update.Guild',
            side_effect=MockGuild)
def test_guildName(mGuild, mSession, mApp, mGldByName):
    mGuild.query.filter_by.return_value.first.return_value = None
    assert guildName('name') == ['name1string11']

    mGuild.query.filter_by.return_value.first.return_value = MockGuild(
        'name', 'id', 1)
    assert guildName('name') == ['nameid1']
