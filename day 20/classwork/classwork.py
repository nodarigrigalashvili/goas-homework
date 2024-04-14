hello = [1,5,6,2,4,7,3,8]
heya = []

for i in hello:
    if i % 2 == 0:
        heya.append(i)
print(heya)


hello2 = [1,5,6,2,4,7,3,8]

for i in range(len(hello2)):
    if i < hello2[-1]:
        if i % 2 != 0:
           hello2.pop(i)
    else:
        i - 1

    
print(hello2)
