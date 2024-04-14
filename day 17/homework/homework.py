def function(list):
    for i in range(len(list)):
        if i < 2:
            print(list.upper())
            if i < 3:
                print(list.lower())
                if i < 4:
                   print(list.capitalize())
    print(list.find("o"))
        

function("hello")

def sneaky(list,hello):
    for i in range(len(list)):
        if list[i] == hello:
            return i

print(sneaky(["name1","name2","name3"], "name2"))

def func(string, char):
    result = ' '
    for word in string:
        result = result + word + char
    return result[0:-1]

print(func(["big", "small", "large"], "-"))




    

        
