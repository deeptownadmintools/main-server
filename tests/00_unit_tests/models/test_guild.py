import mock
from dtat.models.guild import Guild


@mock.patch('dtat.app.db.Model')
@mock.patch('dtat.app.db.relationship', return_value=None)
def test_guild(mModel, mApp):
    g = Guild('name',2,3)
    assert g.name == 'name'
    assert g.rockbiteId == 2
    assert g.level == 3
    assert g.keys() == [
            'id',
            'name',
            'level',
        ]
    assert Guild.keys() == [
            'id',
            'name',
            'level',
        ]
    g.id=1
    assert g.list() == [
            1,
            'name',
            3,
        ]
