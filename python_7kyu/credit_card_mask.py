#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

#Practice problem to mask credit card information
#ex: "4556364607935616" --> "############5616"

# return masked string
def maskify(cc):
    return_string = ""
    index = 0
    while index < len(cc) - 4:
        return_string += "#"
        index += 1
    while index < len(cc):
        current_letter = cc[index]
        return_string += current_letter
        index += 1
    return return_string