def playerDonationMatch(timestamp):
    """
    Matches player name and donations and returns them formated.
        :param timestamp: TimeStamp object 
        :returns: {
            'from': 'Dawn of time',
            'to': 'date',
            'keys': [
                'name',
                'donated',
                'received',
            ],
            'data': [...]
        }
    """
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
