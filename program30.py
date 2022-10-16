class Deque:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue_first(self,value):
        self.list.insert(0,value)

    def enqueue_last(self,value):
        self.list.append(value)

    def dequeue_first(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            self.list.pop(0)


    def dequeue_last(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            self.list.pop()

    def front(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            return self.list[0]

    def rear(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            return self.list[-1]

    def print_queue(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            print("Deque Elements -> ",self.list)



d = Deque()
for i in range(1,11):
    d.enqueue_last(i)
d.print_queue()
d.enqueue_first(0)
d.print_queue()
d.dequeue_first()
d.print_queue()
d.dequeue_last()
d.print_queue()
print(d.front())
print(d.rear())