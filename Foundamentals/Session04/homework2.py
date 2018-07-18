print ("Hello my name is Hiep and these are my ship size")
size = [5,7,300,90,24,50,75]
print(size)
i= int(max(size))
print("now my biggest ship has size",i,"let's shear it")
size[2] = 8
print("after shearing , here is my flock")
print(size)
for _ in range (4) :

    for i in range (0,6,1) :
        size[i] = size[i] + 50

    print("one month has passed , now here is my flock")
    print(size)
    j = int(max(size))
    print("now my biggest ship has size",j,"let's shear it")
    index = size.index(max(size))
    size[index] = 8
    print("after shearing , here is my flock")
    print(size)






