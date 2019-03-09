from dtat.services.rockbite import guildById
from dtat.models import Player, Count, TimeStamp
from dtat import app
from datetime import datetime


def guildObj(guild):
    """
    Updates guild data in database
        :param guild: model object containing id and rockbite object id
    """
    playerIds = []

    data = guildById(guild.rockbiteId)

    timeStamp = TimeStamp(guild.id, data['server_time'])
    app.db.session.add(timeStamp)

    data = data['result']

    guild.name = data['guild_name']
    guild.level = data['guild_level']

    app.db.session.commit()

    for a in data['members']:
        player = Player.query.filter_by(rockbiteId=a['user_id']).first()

        # print(a)
        if 'last_online' not in a or int(a['last_online'][:4]) < 2019:
            if player is None:
                player = Player(guild.id, a['user_name'], a['user_id'])
                app.db.session.add(player)
            count = Count(timeStamp.id, player.id, a['donations'], 0)
            app.db.session.add(count)
            app.db.session.commit()
            playerIds.append(player.id)
            continue

        if 'oil_building_count' not in a:
            a['oil_building_count'] = 0
        if 'chemistry_mining_station_count' not in a:
            a['chemistry_mining_station_count'] = 0
        if 'last_event_donation' not in a:
            a['last_event_donation'] = 0
        if 'received_donation' not in a:
            a['received_donation'] = 0

        if player is None:
            player = Player(guild.id, a['user_name'],
                            a['user_id'], a['last_online'],
                            a['level'], a['depth'], a['miners_count'],
                            a['chemistry_mining_station_count'],
                            a['oil_building_count'], a['crafters_count'],
                            a['smelters_count'], a['last_event_donation'])
            app.db.session.add(player)
            app.db.session.commit()
        else:
            player.guild_id = guild.id
            player.name = a['user_name']
            player.lastOnline = datetime.strptime(
                a['last_online'],
                "%Y-%m-%dT%H:%M:%S.%fZ")
            player.level = a['level']
            player.depth = a['depth']
            player.mine = a['miners_count']
            player.chemMine = a['chemistry_mining_station_count']
            player.oil = a['oil_building_count']
            player.crafters = a['crafters_count']
            player.smelters = a['smelters_count']
            player.lastEventDonation = a['last_event_donation']

        count = Count(timeStamp.id, player.id, a['donations'],
                      a['received_donation'])
        app.db.session.add(count)
        playerIds.append(player.id)

    app.db.session.commit()
    return playerIds
