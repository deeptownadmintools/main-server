def playerDonDiffMatch(timestamp1, timestamp2):
    list = []
    if (timestamp1.id < timestamp2.id):
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
                    int(countA.donated - countB.donated),
                    int(countA.received - countB.received),
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
