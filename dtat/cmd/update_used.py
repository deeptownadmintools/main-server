from dtat import app
from dtat.services.update import updateUsed
from datetime import datetime


@app.cli.command()
def update_used():
    updateUsed()
    print(datetime.utcnow())
