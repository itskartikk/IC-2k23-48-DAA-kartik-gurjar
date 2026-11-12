def binary_s(arr,low,high,key):
    mid = (low + high)//2
    if low > high:
        return -1
    elif arr[mid]== key:
        return mid
    elif arr[mid]>key:
        return binary_s(arr,low,mid-1,key)
    else :
        return binary_s(arr,low+1, high , key)

arr = [10,20,30,40,50,60,70,80,90]
key= 80
v1 = binary_s(arr,0,len(arr)-1,key)
if v1 != -1:
    print(key,"found at index", v1)   
else:
    print("not found")        

