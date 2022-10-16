class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.top = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self,value):
        new_node = Node(value)
        self.size += 1

        if self.isEmpty():
            self.head = new_node
            self.top = new_node

        else:
            self.top.next = new_node
            self.top = new_node


    def pop(self):
        if self.isEmpty():
            return "Empty List..."

        else:
            self.size -= 1
            prev = self.head
            last = self.head.next
            
            while last.next is not None:
                prev = prev.next
                last = last.next
            data=last.data
            prev.next = None
            self.top = prev
            return data


    def print_list(self):
        if self.head is None:
            return "Empty Stack...."
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end='-->')
                temp = temp.next
            print("Null")
            


S = Stack()
for i in range(1,8):
    S.push(i)
S.print_list()
print(S.pop())
S.print_list()
