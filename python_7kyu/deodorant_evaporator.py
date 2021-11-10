def evaporator(content, evap_per_day, threshold):
	c = content
    days = 0
    while c < threshold/100 * content:
        days += 1
    return 0