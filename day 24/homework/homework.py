wow = ["google", True, 14, "wow", 10]
hello = 0
for i in range(len(wow)):
    if type(wow[i]) == type(i):
        hello = hello + wow[i]
print(hello)


Dang = ["goog", 23, 0.4, False, "fasp", "lol", 1.5, 0.1, 10.5]
heya = 0
for i in Dang:
    if type(i) == int:
        heya = heya + i
    if type(i) == float:
        heya = heya + i
    
print(heya)

heya1 = []
number = int(input("enter a number here: "))
for i in range(1, number + 1):
    if int(number / i) * i == number:
        heya1.append(i)
print(heya1)


heya2 = ''
name = input("enter you name here: ")
for i in name:
    if i != i.upper():
        heya2 = heya2 + i.upper()
    else:
        heya2 = heya2 + i.lower()
print(heya2)

Listofnumbers = [1,1,1,1,3,4,5,6]
world = 0
lol = 0
for i in Listofnumbers:
    if i == world:
        lol = lol + 1
    world = world + i
print(lol)
     

    



    