
def shellsort(data, length):
    gap = length//2
    while gap > 0:
        for index in range(gap, length):
            temp = data[index]
            index2 = index
            
            while index2 >= gap and data[index2 - gap] > temp:
                data[index2] = data[index2 - gap]
                index2 -= gap
            data[index2] = temp
        gap //=2
    
arr = [3,6,5,1,3,6,7,8,9,6,5,6,4,4,3,4,2,2,4,8,8,5,3,5]
shellsort(arr, len(arr))
print(arr)
