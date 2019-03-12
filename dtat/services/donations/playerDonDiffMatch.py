def playerDonDiffMatch(timestamp1, timestamp2):
    list = []
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

    return {
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': list
    }
