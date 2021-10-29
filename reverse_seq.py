#Write a function that returns array of ints from n to 1 where n > 0
def reverse_seq(n):
    m = n
    array = []
    while m!= 0:
        array.append(m)
        m-= 1
    return array