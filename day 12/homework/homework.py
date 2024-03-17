number = 0

negatives = int(input("please enter a negative number: "))

while negatives >= 0:
    print("thats not a negative number")
    negatives = int(input("please enter a negative number: "))

number2 = -1
list2 = []
number3 = -1
while negatives != number3:
    negatives = negatives + 1
    list2.append(number2)
    number2 = number2 + -1 
print(list2)
        
Username = input("please enter your username: ")

Lastname = input("please enter your last name: ")

age = int(input("please enter your age: "))

place = input("where do you live?: ")

list = []

list.append(Username)

print(list)

list.append(Lastname)

print(list)

list.append(age)

print(list)

list.append(place)

print(list)

print(list[0:2])

print(list[1:3])

print(list[0:3])

print(list[1:4])

list3 = ["nodari", "grigalashvili"]

print(list3[0:2])

#i dont have many favorite films so instead ill use my favorite food 

list4 = ["carrot", "chicken broth", "pasta", "orange", "green plum", "peach"]


print(list4[0:3])
print(list4[1:2])
print(list4[3:4])
print(list4[0:6])

print(list4[-4:-2])
print(list4[-3:-1])
print(list4[-4:-2])
print(list4[-6:-4])


Academy = input("Please write down the name of the academy: ")

AcademyG = Academy.__contains__("g" or "G")

if AcademyG == True:
    print("if goa meets your needs then Goa's probably the best option for you")
else:
    print("You chose the wrong path! good luck! Yes every academy starting with g is automatically Better")




    

    
    

