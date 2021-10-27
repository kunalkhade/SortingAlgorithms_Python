def selectionSort(data):
    for scanIndex in range(len(data)):
        minIndex = scanIndex
        
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]
            
arr = [5,1,2,3,6,4,4,5,4,1,2,5,5,6,9,74,1,2,5,6,8,5,1,1,5,2,3,96,41,2,3]
selectionSort(arr)
print(arr)

