list = [1,2,3,4,5,6,7,8,9,]
heya = int()
for i in list:
    heya = heya + i
print(heya)
heya = heya / len(list)

print(heya)
minus =[]
plus = []
numbers = [1,64,-354,154,-43,-1,654,0,-421,3643]
for i in numbers:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
print(minus)
print(plus)