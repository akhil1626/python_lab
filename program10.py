def binary(list,lb,ub,key):
    while(lb<=ub):
        mid=lb+(ub-lb)//2
        if(list[mid]==key):
            return mid
        elif key<list[mid]:
            ub=mid-1
        else:
            lb=mid+1
    return -1
        

list=[1,2,3,4,5,6,7,8,9]
key=int(input("enter value to be searched "))
index=binary(list,0,len(list)-1,key)
if index==-1:
    print("element not found")
else:
    print("element found at index ",index)