from dtat.models import Guild, Player, Count, TimeStamp
from dtat.exceptions import DbException, RockbiteException
from dtat.services.rockbite import guildByName, guildById
from dtat import app
from datetime import datetime, timedelta


def guildObj(guild, respond=False, update=False):
    """
    Updates guild data in database
        :param guild: instance of Guild containing id and rockbite object id
        :param respond: nothing will be returned if False
        :param update: if True guild will be marked for periodical updates
        :returns: {
            'players': [...],
            'guild': obj,
            'timeStamp': obj
            }
    """
    lastTimeStamp = TimeStamp.query.filter_by(
        guild_id=guild.id).order_by(TimeStamp.id.desc()).first()

    now = datetime.utcnow()

    if (lastTimeStamp is not None and lastTimeStamp.date >
            now - timedelta(minutes=10)):
        if not respond:
            return
        return {
            'players': guild.players,
            'guild': guild,
            'timeStamp': lastTimeStamp
        }

    if update:
        guild.lastVisited = datetime.utcnow()

    playerIds = []

    data = guildById(guild.rockbiteId)

    timeStamp = TimeStamp(guild.id, now)
    app.db.session.add(timeStamp)

    data = data['result']

    guild.name = data['guild_name']
    guild.level = data['guild_level']

    app.db.session.commit()

    for a in data['members']:
        player = Player.query.filter_by(rockbiteId=a['user_id']).first()

        if 'last_online' not in a:
            a['last_online'] = "2018-1-1T00:00:00.00Z"
        if 'level' not in a:
            a['level'] = 0
        if 'depth' not in a:
            a['depth'] = 0
        if 'miners_count' not in a:
            a['miners_count'] = 0
        if 'chemistry_mining_station_count' not in a:
            a['chemistry_mining_station_count'] = 0
        if 'oil_building_count' not in a:
            a['oil_building_count'] = 0
        if 'crafters_count' not in a:
            a['crafters_count'] = 0
        if 'smelters_count' not in a:
            a['smelters_count'] = 0
        if 'jewellery_building_slot_count' not in a:
            a['jewellery_building_slot_count'] = 0
        if 'chemistry_building_slot_count' not in a:
            a['chemistry_building_slot_count'] = 0
        if 'green_house_building_slot_count' not in a:
            a['green_house_building_slot_count'] = 0
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
                            a['smelters_count'],
                            a['jewellery_building_slot_count'],
                            a['chemistry_building_slot_count'],
                            a['green_house_building_slot_count'],
                            a['last_event_donation'])
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
            player.jewel = a['jewellery_building_slot_count']
            player.chemStation = a['chemistry_building_slot_count']
            player.greenHouse = a['green_house_building_slot_count']
            player.lastEventDonation = a['last_event_donation']

        timeStamp.counts.append(Count(timeStamp.id, player.id, a['donations'],
                                      a['received_donation']))
        playerIds.append(player.id)

    app.db.session.commit()

    players = Player.query.filter_by(guild_id=guild.id).all()
    if len(players) != len(playerIds):
        for a in players:
            if a.id not in playerIds:
                a.guild_id = None
        app.db.session.commit()
    if respond:
        return {
            'players': players,
            'guild': guild,
            'timeStamp': timeStamp
        }


def guildId(id, respond=False, update=False):
    """
    Updates guild data in database
        :param id: database id of a guild
        :param respond: nothing will be returned if False
        :returns: {
            'players': [...],
            'guild': obj,
            'timeStamp': obj
            }
        :raises DBException: DBException is raised, when guild with specified
            id was not found.
    """
    guild = Guild.query.get(id)
    if guild is None:
        raise DbException(404, "Guild was not found", ["id"])
    return guildObj(guild, respond, update)


def guildName(guildName):
    """
    Updates list of guilds
        :param guildName: (partial) guild name
        :returns: list of added guild's ids
    """
    data = guildByName(guildName)['result']
    ids = []
    for a in data:
        guild = Guild.query.filter_by(rockbiteId=a['guild_id']).first()
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


def updateAll():
    """
    Updates every guild's data in database
    """
    guilds = Guild.query.all()
    for a in guilds:
        guildObj(a)


def updateUsed():
    """
    Updates every used guild's data in database
    """
    guilds = Guild.query.filter(
        Guild.lastVisited >= datetime.utcnow() - timedelta(30)).all()
    for a in guilds:
        print(a.name, a.id)
        try:
            guildObj(a)
        except RockbiteException as e:
            print(datetime.utcnow(), " - ", a.name, a.id, " - ", e.message)
