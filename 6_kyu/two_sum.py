def two_sum(numbers, target):
    correct = [2]
    index = 0
    while correct[0] + correct[1] != target:
        current = numbers[index]
        found = target - current
        f = current.find(found)
        if f != -1:
            correct[0] = current
            correct[1] = numbers[f]
        index += 1
    return correct