def gimme(input_array):
    value = sorted((input_array[0],input_array[1],input_array[2]))[1]
    answer = 0
    for number in input_array:
        if number == value:
            break
        else:
            answer += 1
    return answer