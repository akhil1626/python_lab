list=[]
file_name=input("enter the file name")
with open (file_name,"r") as f:
    for i in f:
        list.append(i.strip("\n"))
list.sort()
print(list)
