from dtat import app


def removeGuild(guild):
    app.db.session.delete(guild)
    app.db.session.commit()
