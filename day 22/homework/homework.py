def manual_pop(List, index = 0):
    Hello = []
    for i in range(0, len(List)):
       if i != index:
           Hello.append(List[i])
    return Hello
print(manual_pop(["hello", "byeee", "woaa", "nice"], ))

def manual_count(List, element = "hello"):
    num = 0
    for i in List:
        if i == element:
            num = num + 1
    return num
        
    
print(manual_count(["woah", "nice", "woah", "nice", "nice", ], "nice" ))



