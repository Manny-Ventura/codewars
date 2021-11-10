#Write a function that turns a string segmented by '-' or '_'
#and have it turn to camel case
#https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/python
def to_camel_case(text):
    final = ''
    index = 0
    while index < len(text):
        if text[index -1] == '-' or text[index-1] == '_':
            final += text[index].upper()
        else:
            if text[index] != '-' and text[index] != '_':
                final += text[index]
        index += 1
    return final