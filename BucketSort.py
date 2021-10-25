
def bucketsort(arr, buckets):
    max_ele = max(arr)
    min_ele = min(arr)
    rnge = (max_ele - min_ele)/buckets
    temp = []
    
    for i in range(buckets):
        temp.append([])
        
    for i in range(len(arr)):
        diff = (arr[i] - min_ele)/rnge - int((arr[i] - min_ele)/rnge)
        
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele)/rnge)-1].append(arr[i])
        else:
            temp[int((arr[i]-min_ele)/rnge)].append(arr[i])
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1
arr = [9.3, 5.2, 3.4, 0.9, 1.9, 3.4, 1.5, 4.3]
buckets =  4          
bucketsort(arr, buckets)
print(arr)