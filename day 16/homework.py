def word(hello,bye):
    return hello + " " + bye

x = word("hello","bye")

print(x)

def colors(color1,color2):
    if color1 == "yellow" or "Yellow":
        if color2 == "red" or "Red":
            print("orange")

colors("yellow","red")

def window(window1,window2):
    return window1 + window2

print(window("clos","et"))

def wow(jeez,dang):
    if jeez[0] == "j":
        print("jeez")
    if dang[-1] == "g":
        print("dang")

print(wow("jewlery","bing"))

def clouds():
    big = "cirrocumulus cloud"
    z = "which cloud is the"
    return big, z

big, z = clouds()
print(z,big)

def even(List):
    list_even = list([])
    for i in range(len(List)):
        if ((List[i] % 2) == 0):
            list_even.append(List[i])
    car = list_even[0] + list_even[1]
    return car,
            

print(even([1,2,3,4,5]))

def even(List):
    list_even = list([])
    for i in range(len(List)):
        if ((List[i] % 2) != 0):
            list_even.append(List[i])
    car1 = list_even[0] + list_even[1] + list_even[2]
    car = []
    car.append(car1)

    list_even1 = list([])
    for i in range(len(List)):
        if ((List[i] % 2) == 0):
            list_even1.append(List[i])
    cat1 = list_even1[0] + list_even1[1]
    cat = []
    cat.append(cat1)
    return car + cat
            

print(even([1,2,3,4,5]))

def number(last):
    zero = 0
    for i in last:
       zero = zero + 1
    return zero
print(number([1,2,3,4,5]))

def hello(wow):
    well = " "
    return well.join(wow)
    

print(hello("nice"))


def hello(why):
    well = "amazing work"
    return well.replace("work", "dam")

print(hello("dam"))





        
        

    



    
        


