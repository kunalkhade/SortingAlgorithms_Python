#Heap Sort Algorithm
def CreateHeap(data, length, index):
    largest = index
    left = 2*index + 1
    right = 2 * index + 2
    
    if left < length and data[index] < data[left]:
        largest = left
    
    if right < length and data[largest] < data[right]:
        largest = right
    
    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        CreateHeap(data, length, largest)
        
def heapSort(data):
    length = len(data)
    for index in range(length//2 -1, -1, -1):
        CreateHeap(data, length, index)
    for index in range(length -1, 0, -1):
        data[index], data[0] = data[0], data[index]
        CreateHeap(data, index, 0)
        
    print(data)
    
arr = [2,6,9,3,4,1,0,3,6,5,4,2]
heapSort(arr)
