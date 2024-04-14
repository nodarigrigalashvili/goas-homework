
name1 = input("enter your name :")
name2= name1.lower()
if name1 == name2:
    print(name1)


num = 0
hello = input("please enter a word :")
hello1 = hello.upper()
hello0 = ' '
for i1 in hello:
   for i in hello1:
      hello0 = hello0 + i
   while hello != hello1:
      hello = input("please enter the word again :") 
      num = num + 1
print(num)

name = "Nodo"
if len(name) >= 5:
   print(name.upper())
else:
   print(name.lower())


def upp(list):
    list1 = []
    for x in list:
        list1.append(x.capitalize())
    return list1

print(upp(["nodar","grigalashvili"]))


name = input("please enter your name :")
surname = input("please enter your surname :")
help = []
hi = "h"
for i in hi:
   help.append(name)
   help.append(surname)
hello = help[1]
hello1 = help[0]
print(hello1[0:1].upper()+"."+hello[-1:].upper())

word = input("please enter an uppercase word :")
letter = ''

for i in range(len(word)):
   if i % 2 == 0:
      letter = letter + word[i].upper()
   else:
      letter = letter + word[i].lower()

print(letter)

string = []

for i in range(5):
    word = input("enter a word :")
    string.append(word)

print(string)


character = input("please enter a character :")

woop = ''

for i in range(len(string)):
   if i % 2 == 0:
      woop = woop + string[i] + character

woop = woop[:-1]

yet = input("please enter a word :")
yet1 = input("please enter a letter :")

print(yet.find(yet1))
hello = 0
for i in yet:
   hello = hello + 1
   if i == yet1:
      print(hello)
      exit()
   else:
      print("-1")
      exit()




      
   












    
    
