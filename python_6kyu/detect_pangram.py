#A pangram is a sentence that contains every single letter of the alphabet
#Write a program to see if a string is a program or not: return True or False

import string

def is_pangram(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    values = [False]*26
    splits = s.split()
    #Work with each word in a split
    for word in splits:
        index = 0
        #Go through each letter in each word
        while index < len(word):
            #Account for anything that isnt a letter
            try:
                b=alphabet.index(word[index])
            except ValueError:
                "Do Nothing"
            else:
                values[b] = True
            index += 1
    
    
    
    
    
    pangram = True
    for value in values:
        if value == False:
            pangram = False

    return pangram

print(is_pangram("The quick, brown fox jumps over the lazy dog"))