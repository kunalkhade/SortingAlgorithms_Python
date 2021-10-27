
def quicksort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quicksort(data, left, pivot-1)
        quicksort(data, pivot + 1, right)
        
def partition(data, left, right):
    pivot = data[left]
    leftIndex = left + 1
    rightIndex = right 
    
    while True:
        while leftIndex <= rightIndex and data[leftIndex] <= pivot:
            leftIndex += 1
        while rightIndex >= leftIndex and data[rightIndex] >= pivot:
            rightIndex -= 1
        if rightIndex <= leftIndex:
            break
        data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]
       # print(data)
    data[left], data[rightIndex] = data[rightIndex], data[left]
  #  print(data)
    
    return rightIndex
    
arr = [4,6,7,4,5,2,1,9,7,8,4,2]
n = len(arr)
quicksort(arr, 0, n-1)
print(arr)