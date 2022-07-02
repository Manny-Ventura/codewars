#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

#test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
def filter_list(l):
    new_list = []
    for i in l:
        if type(i) != str:
            new_list.append(i)
    return new_list
filter_list(test)