#Write a function that returns the complementary strand of DNA
def DNA_strand(dna):
    final = ''
    for letter in dna:   
        if letter.upper() == 'A':
            final += 'T'
        elif letter.upper() == 'T':
            final += 'A'
        elif letter.upper() == 'C':
            final += 'G'
        elif letter.upper() == 'G':
            final += 'C'
    return final