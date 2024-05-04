
Listofnumbers = [1,1,1,1,3,4,5,6]
world = 0
lol = 0
for i in Listofnumbers:
    if i == world:
        lol = lol + 1
    world = world + i
print(lol)
