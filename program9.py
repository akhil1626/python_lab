def binary(list,lb,ub,key):
    if(lb<=ub):
        mid=lb+(ub-lb)//2
        if list[mid]==key:
            return mid
        elif key<list[mid]:
             return binary(list,lb,mid-1,key)
        else:
             return binary(list,mid+1,ub,key)
    return -1

list=[1,2,3,4,5,6,7,8,9]
key=int(input("enter the value to be searched in the list "))
index=binary(list,0,len(list)-1,key)
if index==-1:
    print("value not found.....!")
else:
    print("value found at index ",index)




