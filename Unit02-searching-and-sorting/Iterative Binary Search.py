def binary_s(arr,key):
    low = 0 
    high =len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key :
            return mid
        elif key <  arr[mid]:
            high = mid -1
        else:
            low = mid +1 
    return -1

arr = [10,20,30,40,50,60,70]
v1= binary_s(arr,50)
if v1 != -1:
    print("element found at index", v1)
else:
    print("not found") 
