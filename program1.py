final=[]
n=int(input("enter the number of students "))
for i in range(n):
    t=[]
    t.append(input("enter the student name "))
    t.append(int(input("enter the ages ")))
    final.append(t)

final.sort(key=lambda x:x[1])



print(final)    
