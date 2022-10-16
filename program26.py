# class stack:
#     def __init__(self):
#         self.list = []
#     def push(self,element):
#         self.list.append(element)
    
#     def reverse(self):
#         print("in reverse order.....")
#         for i in self.list[::-1]:
#             print(i,end=" ")
#         print()
#     def display(self):
#         for i in self.list:
#             print(i, end = " ")
#         print()
# s = stack()
# print("enter the no of your string(s)")
# n = int(input())

# for i in range(n):
#     s.push(input("enter your string : "))
# s.display()
# s.reverse()

class stack:
    def __init__(self):
        self.list = []
    def push(self,element):
        self.list.append(element)
    
    def reverse(self):
        print(self.list[ ::-1])
        print()
    def display(self):
        print(self.list)
        print()
s = stack()
print("enter the no of your string(s)")
n = int(input())

for i in range(n):
    s.push(input("enter your string : "))
s.display()
s.reverse()

