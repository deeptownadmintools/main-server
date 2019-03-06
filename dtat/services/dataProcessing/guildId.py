from dtat.services.rockbite import guildById
from dtat.models import Guild, Player, Count, TimeStamp
from dtat import app
from datetime import datetime


def guildId(id, rockbiteId):
    data = guildById(rockbiteId)['result']

    guild = Guild.query.get(id)
    guild.name = data['guild_name']
    guild.level = data['guild_level']
    app.db.session.commit()

    for a in data['members']:
        player = Player.query.filter_by(rockbiteId=a['user_id']).first()
        if player is None:
            player = Player(id, a['user_name'], a['user_id'], a['last_online'],
                            a['level'], a['depth'], a['miners_count'],
                            a['chemistry_mining_station_count'],
                            a['oil_building_count'], a['crafters_count'],
                            a['smelters_count'], a['last_event_donation'])
            app.db.session.add(player)
            app.db.session.commit()
        else:
            player.name = a['user_name']
            player.lastOnline = a['last_online']
            player.level = a['level']
            player.depth = a['depth']
            player.mine = a['miners_count']
            player.chemMine = a['chemistry_mining_station_count']
            player.oil = a['oil_building_count']
            player.crafters = a['crafters_count']
            player.smelters = a['smelters_count']
            player.lastEventDonation = datetime.strptime(
                a['last_event_donation'],
                "%Y-%m-%dT%H:%M:%S.%fZ")
            app.db.session.commit()
