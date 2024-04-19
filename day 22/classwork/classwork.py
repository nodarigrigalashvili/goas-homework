

def manual_pop(list,hello):
    heya = []
    
    for i in range(0, len(list)):
        if i != hello:
            heya.append(list[i])
    return heya 
    
print(manual_pop([1,2,3,4,5,6,7,8,9,10], 0))

def manual_count(heya,hello):
    num = 0
    for i in heya:
      if i == hello:
          num = num + 1
    return num
          
print(manual_count([1,2,2,3,4,5,3,4,2],2))

def manual_index(list, hello):
    for i in range(len(list)):
        if list[i] == hello:
            return i
    return -1
    
print(manual_index(["hello","wow","lucky"], "hello"))

