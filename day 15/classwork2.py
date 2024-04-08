
def math1(number1,number2):
    print(number1 + number2)

math1(2,9)

def math2(number3,number4):
    print(number3 - number4)

math2(10,3)

def math3(number5,number6):
    print(number5 * number6)

math3(2,2)

def math4(number7, number8):
    print(number7 / number8)

math4(32,4)
    

def area(width,length):
    print(width * length)

area(8,4)

def area1(height,length,width,depth):
    print(height * width, length * depth)

area1(3,4,6,2)


def number(well,): # [1,2,3,4,5]
    sum = 0

    for i in well:
        sum = sum + i

    print(sum)
    
number([1,2,3,4,5])


def minmax(list):
    min = list[0]
    max = list[0]

    for i in list:
        if min > i:
            min = i
        if max < i:
            max = i
    
    print(min,max)

minmax([1,2,3,4,5])