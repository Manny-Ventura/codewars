def open_or_senior(data):
    list = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            list.append('Senior')
        else:
            list.append('Open')
    return list