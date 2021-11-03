#Complete the solution so that it returns true if the first argument(string) 
# passed in ends with the 2nd argument (also a string).
#Example solution('abc','bc') returns true
#Example solution('abc','d') erturns false
def solution(string, ending):
    answer = string.find(ending)
    if ending == '':
        return True
    else:
        if answer != -1 and string[-1] == ending[-1]:
            return True
        else:
            return False