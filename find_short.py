#Find the shortest value in the input string and return the shortest word's length
def find_short(s):
    splits = s.split()
    length = len(splits[0])
    value = splits[0]
    index = 1
    while index < len(splits):
        current = splits[index]
        if len(current) < length:
            length = len(current)
            value = current
        index += 1
    return length