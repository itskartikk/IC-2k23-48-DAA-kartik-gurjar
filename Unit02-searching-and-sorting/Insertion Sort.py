def ins_sort(arr):
    for i in range (1, len(arr)):
        key = arr [i]
        j = i -1 
        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]= key 
arr = [5,2,9,1,7,4]
ins_sort(arr)
print(arr)                    
