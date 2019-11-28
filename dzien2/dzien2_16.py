elements = range(5,50,1)
index = -1
while(True):
    index += 1
    if(index % 2 == 0):
        continue
    print(index, elements[index])
    if(index == len(elements) - 1):
        break