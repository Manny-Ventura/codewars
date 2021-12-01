#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

#Your goal in this kata is to implement a difference 
#which subtracts one list from another and returns the result.

#If a value is present in b, all of its occurrences must be removed from the other:

def array_diff(a, b):
    final = []
    for number in a:
        allowed = None
        for value in b:
            if number == value:
                allowed = False
        if allowed != False:
            final.append(number)
    return final
print(array_diff([1,2,3],[2]))