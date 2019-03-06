from dtat.services.rockbite import guildByName
from dtat.models import Guild
from dtat import app


def guildName(guildName):
    data = guildByName(guildName)['result']
    ids = []
    for a in data:
        guild = Guild.query.filter_by(rockbiteID=a['guild_id']).first()
        if guild is None:
            guild = Guild(a['guild_name'], a['guild_id'], a['level'])
            app.db.session.add(guild)
            app.db.session.commit()
        else:
            guild.name = a['guild_name']
            guild.level = a['level']
            app.db.session.commit()
        ids.append(guild.id)
    return ids