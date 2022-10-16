start=1
end=int(input("enter the ending range"))
print("the prime numbers between ",start,"and",end,"are")
for i in range(start+1,end+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if(flag==0):
        print(i,end="  ")

