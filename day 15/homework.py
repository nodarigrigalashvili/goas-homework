def palindrome(Word):
    worder = Word[::-1]
    if Word == worder:
        print(worder)


palindrome("mom")

def initials(fullname):
    split_full = fullname.split(" ")
    
    name = split_full[0]
    lastname = split_full[1]

    result = name[0] + "." + lastname[0]

    print(result)

initials("nodar grigalashvili")


def avrg(number):
    jami = sum(number)
    print(jami)
    result = jami / len(number)
    print(result)

avrg([1,2,3,4,5])


def pal(word):
    rev_word = " "

    for i in range(len(word) - 1, -1, -1):
        rev_word = rev_word + word[i]

    print(rev_word == word)

pal("radar")


def remover(word):
    without = " "

    for i in word:
        if i != " ":
            without = without + i
    
    print(without)

remover("nodar grigalashvili")

def nepositive(number):
    sum = 0
    quantity = 0

    for i in number:
        if i >= 0:
            i = i + sum
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

    nepositive([1,2,3,-1,-2,-3])



    
    
    












