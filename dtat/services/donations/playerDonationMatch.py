def playerDonationMatch(timestamp):
    list = []
    for count in timestamp.counts:
        list.append([
            count.player.name,
            int(count.donated),
            int(count.received),
        ])
    return {
        'date': timestamp.date,
        'keys': [
            'name',
            'donated',
            'received',
        ],
        'data': list
    }
