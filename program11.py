def insertion(list):
    n=len(list)
    for i in range(1,n):
        current=list[i]
        j=i-1
        while (j>=0 and current<=list[j]):
            list[j+1]=list[j]
            j-=1
        list[j+1]=current

list=[7,8,3,1,2]
insertion(list)
print(list)
