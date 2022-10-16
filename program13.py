def selection(list):
    n=len(list)
    for i in range(0,n):
        smallest=i
        for j in range(i+1,n):
            if(list[j]<=list[smallest]):
                smallest=j
        list[i],list[smallest]=list[smallest],list[i]
list=[7,8,3,1,2]
selection(list)
print(list)