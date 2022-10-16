class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enqueue(self,value):
        new_node = Node(value)
        self.size += 1

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Empty Queue...\n"
        else:
            self.front = self.front.next
            self.size -= 1
    def frontt(self):
        if self.front is None:
            return "empty queue"
        else:
            return self.front.data  


    def print_list(self):
        if self.front is None:
            return "Empty Queue...."
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,end='-->')
                temp = temp.next
            print("Null")


q = Queue()
for i in range(1,8):
    q.enqueue(i)
q.print_list()
q.dequeue()
q.print_list()
print(q.frontt())