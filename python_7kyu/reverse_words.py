#Complete function that accepts a string as a parameter
#and reverses each word in the string
def reverse_words(text):
    n = len(text)
    text = list(text)

    # 2 pointers
    # as 2 corners
    start = 0 
    end = n - 1

    #move both pointers
    while(start < end):
        # If charatcer at start
        # or end is space,
        # ignore it
        if(text[start])





print(reverse_words("I am a gay sailor!"))