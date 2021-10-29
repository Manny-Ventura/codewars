#Given a string of words, find the highest scoring word
#Scoring --- a = 1, b = 2, etc.
#return the highest scoring word as a string
def value(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    score = 0
    highest = ''
    for letter in word:
        if letter != ' ':
            score +=  alphabet.index(letter.lower()) + 1

    return score

def high(x):
    highest = 0
    str = ''
    current = value('I am a gay soldier')
    print(current)
            
    return str
high('Hello')
