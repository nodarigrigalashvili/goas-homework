# 1. 
def litres(time):
    return int(time * 0.5)
# 2.
def grow(numbers_list):
    result = 1

    for number in numbers_list:
        result = result * number
    return result
# 3.
def fake_bin(x):
    result = ''

    for char in x:
        if int(char) <5:
            result = result + "0"
        else:
            result = result + "1"
    return result