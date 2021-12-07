#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

#ntervals are represented by a pair of integers in the form of an array. 
# The first value of the interval will always be less than the second value. 
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

#[ [1,2],
#   [6, 10],
#   [11, 15]
#]; // => 9

def sum_of_intervals(intervals):
    #Check if any subtracting number is less than or equal to initial value of an interval
    interval_index = 0
    bank = []
    for interval in intervals:
        min_value = interval[0]
        max_value = interval[-1]
        while min_value <= max_value:
            if min_value not in bank:
                bank.append(min_value)
            min_value += 1
    print(bank)
    bank.sort()
    print(bank)
    count = 0
    value = bank[0]
    index = 1
    while index < len(bank):
        current = bank[index]
        if current - value == 1:
            count += 1
            value = current
        else:
            value = current
        index += 1


    return count

        
print(sum_of_intervals([(1, 5), (6, 10)]))