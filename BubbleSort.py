#Bubble Sort Algorithm

def bubblesort(data):
    length = len(data)
    for i in range(length):
        swapped = False
        for j in range(0, length-i -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                
        if swapped == False:
            break
    print(data)
    
    
mylist = [3,6,8,1,3,2,5,9]
bubblesort(mylist)