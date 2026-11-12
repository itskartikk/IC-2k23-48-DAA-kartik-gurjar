def b_sort(arr,n , i):
    if n == 0:
        return -1
    if i == n-1:
        b_sort(arr , n-1 , 0) 
        return  
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1] = arr[i+1] , arr[i]
    return b_sort(arr , n , i+1) 

arr = [1,6,2,8,4,9,5,7,3]
b_sort(arr,len(arr) , 0)     
print("sorted List is :",arr)   