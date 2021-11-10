def solution(n):
    numbers = [1000,500,100,50,10,5,1]
    numerals = ["M","D","C","L","X","V","I"]
    index = 0
    final= ""
    while index < len(numbers):
        copies = 0
        if n - numbers[index] >= 0 and copies <= 3:
            final += numerals[index]
            copies += 1
        index+= 1
    
def subtraction(n, numbers,numerals):
    if n 
    