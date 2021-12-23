#https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

#Write a function that takes a string of parentheses, and determines 
# if the order of the parentheses is valid. 
# The function should if the string is valid, and false if it's invalid.

def valid_parentheses(string):
    lefts = 0
    rights = 0
    for letter in string:
        if letter is '(':
            lefts += 1
        elif letter is ')':
            rights += 1
        if rights > lefts:
            return False
    if lefts != rights:
        return False
    else:
        return True

test = "hi(hi)()"
valid_parentheses(test)
