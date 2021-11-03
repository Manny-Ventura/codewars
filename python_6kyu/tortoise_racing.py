def radef race(v1, v2, g):
    time = [0,0,0]
    if v1 > v2:
        return None
    else:
        distance = g
        hours = -1
        rate = v2 - v1
        while distance >= 1:
            distance -= rate
            hours += 1
        time[0] = hours
        distance += v2 + v1
        minutes = -1
        while distance >= 1:
            new_rate = (v2 - v1)/60
            distance -= new_rate
            minutes += 1
        time[1] = minutes
        seconds = -1
        while distance > 0:
            newest_rate = new_rate/60
            distance -= newest_rate
            seconds += 1
        time[2] = seconds
        return time

