#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = 0
    final = ''
    while index < len(text):
        #Try to find position in alphabet position exists in 
        try:
            current = text[index].lower()
            b = alphabet.index(current) + 1
        except ValueError:
            #Do Nothing
            ""
        else:
            #Concatenate onto final
            if final == '':
                final += b
            else:
                final == ' ' + b
    return final