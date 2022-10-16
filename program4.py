# filename = input("enter the file name:")
# stringname = input("enter the string:")
# with open(filename,'r') as f:
# 	for i in f.read().splitlines():
#          if stringname in i:
#             print(i)

filename=input(" enter the file name ")
str=input(" enter the string ")

with open (filename,'r') as f:
    new_list=[]
    # list=f.readlines()
    for i in f.readlines():
        if str in i:
            new_list.append(i.strip("\n"))


print(new_list)
   

			
