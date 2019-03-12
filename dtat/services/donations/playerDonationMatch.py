def playerDonationMatch(timestamp):
    list = []
    for count in timestamp.counts:
        list.append([
            count.player.name,
            count.donated,
            count.received,
        ])
    return {
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': list
    }
