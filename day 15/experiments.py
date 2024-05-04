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

print(woop)

#variables can be used both in global and in local in local yuou can only use it in code blocks
