import mock
from datetime import datetime
from dtat.services.update.update_updateUsed import updateUsed


@mock.patch('dtat.services.update.update_updateUsed.datetime')
@mock.patch('dtat.services.update.update_updateUsed.guildObj')
@mock.patch('dtat.services.update.update_updateUsed.Guild')
def test_updateAll(mGld, mGldObj, mDate):
    now = datetime.utcnow()
    mGld.lastVisited=now
    mDate.utcnow.return_value=now
    mGld.query.filter.return_value\
        .all.return_value=[0,1,2,3,4,5]
    updateUsed()
    assert mGldObj.call_count == 6
    
    mGldObj.reset_mock()
    mGld.query.filter.return_value\
        .all.return_value=[]
    updateUsed()
    assert mGldObj.call_count == 0
    
