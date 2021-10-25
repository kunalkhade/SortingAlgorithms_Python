#Insertion Sort Algorithm

def insertionSort(data):
    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]
        minIndex = scanIndex
        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
            
        data[minIndex] = tmp
        
    print(data)
mylist = [3,7,6,4,5,1,9,8,5,6,2]

insertionSort(mylist)