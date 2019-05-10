def playerDonDiffMatch(timestamp1, timestamp2):
    """
    Counts difference in donations between two times, then it matches said
    difference with player names. In case TimeStamp objects are input in a
    wrong order they will be reordered appropriately.
    :param timestamp1: instance of TimeStamp object - from
    :param timestamp2: instance of TimeStamp object - to
    :returns: {
        'from': datetime,
        'to': datetime,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': [...]
        }
    """
    list = []
    if (timestamp1.date > timestamp2.date):
        tmp = timestamp1
        timestamp1 = timestamp2
        timestamp2 = tmp
    for countA in timestamp1.counts:
        matched = False
        for countB in timestamp2.counts:
            if countA.player_id == countB.player_id:
                matched = True
                list.append([
                    countA.player.name,
                    int(countB.donated - countA.donated),
                    int(countB.received - countA.received),
                ])
                break

        if not matched:
            list.append([
                countA.player.name,
                '/',
                '/',
            ])

    return {
        'from': timestamp1.date,
        'to': timestamp2.date,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': list
    }
