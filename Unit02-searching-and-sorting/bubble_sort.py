def b_sort():
    lst=[2,78,4,9,1,8,5,0,]
    for i in range (len(lst)-1):
        done=False
        for j in range(0,len(lst)-i-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]  
                lst[j+1]= temp
                done=True
        if not done:
            break
    print("done!!!", lst)
b_sort()        