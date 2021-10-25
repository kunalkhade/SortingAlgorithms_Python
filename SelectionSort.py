def selectionSort(data):
    for ele in range(0, len(data)-1):
        min_val = ele
        for next_ele in range(ele+1, len(data)):
            if data[next_ele] < data[min_val]:
                min_val = next_ele
        if min_val != ele:
            data[min_val], data[ele] = data[ele], data[min_val]

    print(data)
mylist = [3,7,6,4,5,1,9,8,5,6,2]

selectionSort(mylist)