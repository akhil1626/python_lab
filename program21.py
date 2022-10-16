class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue(self,value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            self.list.pop(0)

    def front(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            return self.list[0]

    def rear(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            return self.list[-1]

    def print_queue(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            print("Queue Elements -> ",self.list)


q = Queue()
for i in range(1,8):
    q.enqueue(i)
q.print_queue()
q.dequeue()
q.print_queue()
print(q.front())
print(q.rear())