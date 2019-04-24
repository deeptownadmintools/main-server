from dtat import app
from dtat.services.update import updateUsed
from datetime import datetime


@app.cli.command()
def update_used():
    """
    Updates all used guilds using command line.
    """
    updateUsed()
    print(datetime.utcnow())
