class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            return self.list[-1]

    def print_stack(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            print("Stack Elements -> ",self.list)


s = Stack()
for i in range(1,8):
    s.push(i)
s.print_stack()
s.pop()
s.print_stack()