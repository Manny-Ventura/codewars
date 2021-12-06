#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

#Complete the solution so that the function will break up camel casing
#using a space between words.

#"camelCasing" => "camel Casing"
#"identifier" => "identifier"
#"" => ""

def solution(s):
    return_string = ""
    for letter in s:
        if letter == letter.lower():
            return_string += letter
        else:
            return_string += f" {letter}"
    return return_string
solution("helloWorld")
