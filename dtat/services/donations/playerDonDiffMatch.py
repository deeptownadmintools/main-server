def playerDonDiffMatch(timestamp1, timestamp2):
    list = []
    print('---')
    for a in timestamp1.counts:
        print(a.donated)
    print('---')
    for a in timestamp2.counts:
        print(a.donated)
    print('---')
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
                    countA.donated - countB.donated,
                    countA.received - countB.received,
                ])
                break

        if not matched:
            list.append([
                countA.player.name,
                '/',
                '/',
            ])
    print('---')
    for a in timestamp1.counts:
        print(a.donated)
    print('---')
    for a in timestamp2.counts:
        print(a.donated)
    print('---')
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
