def playerDonationMatch(timestamp):
    list = []
    for count in timestamp.counts:
        list.append([
            count.player.name,
            int(count.donated),
            int(count.received),
        ])
    return {
        'from': 'Dawn of time',
        'to': timestamp.date,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': list
    }
