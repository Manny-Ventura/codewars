#https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

#You are going to be given an array of integers. 
# Your job is to take that array and find an 
# index N where the sum of the integers 
# to the left of N is equal to the 
# sum of the integers to the right of N. 
# If there is no index that would make this happen, return -1.

def find_even_index(arr):
    index = 0
    while index < len(arr):
        left_indices = sum(i for i in arr if i < index)
        print(left_indices)
        right_indices = sum(i for i in arr if i > index)
        print(right_indices)
        if left_indices == right_indices:
            return index
        index += 1
    return -1
print(find_even_index([1,2,3,4,3,2,1]))