from dtat import app


def removeGuild(guild):
    """
    Removes guild from database.
        :param guild: instance of Guild that will be removed from database
    """
    app.db.session.delete(guild)
    app.db.session.commit()
