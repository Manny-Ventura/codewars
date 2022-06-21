#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    bank_of_numbers = []
    three_index = 3
    five_index = 5
    while three_index < number:
        bank_of_numbers.append(three_index)
        three_index += 3
    while five_index < number:
        bank_of_numbers.append(five_index)
        five_index += 5
    
    total = 0
    result = []
    for num in bank_of_numbers:
        if num not in result:
            result.append(num)
            total += num
    return total