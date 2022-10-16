class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class deque:
    front = None
    rear=None
    size = 0
    def Enqueue(self,elem):
        t= Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.size+=1
        else:
            self.rear.next = t
            self.rear = t
            self.size+=1
    def Enqueue_front(self,elem):
        t = Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.size+=1
        else:
            t.next = self.front
            self.front = t
            self.size+=1
    def Dequeue(self):
        if self.front == None:
            print("the Queue is empty...")
            return
        elif self.front == self.rear:
            delv = self.front.data
            self.front = self.rear = None
            self.size-=1
            return delv
        else:
            delv = self.front.data
            self.front = self.front.next
            self.size-=1
            return delv
    def Dequeue_rear(self):
        if self.front == None:
            print("Queue is empty...")
            return
        elif self.front == self.rear:
            delv = self.front.data
            self.front = self.rear = None
            self.size-=1
            print("the Queue is now empty...")
            return delv
        else:
            temp = self.front
            while temp.next!= self.rear:
                temp = temp.next
            delv = self.rear.data
            temp.next = None
            self.rear = temp
            self.size-=1
    def display(self):
        itr = self.front
        while itr!=None:
            print(itr.data,end="-->")
            itr = itr.next
        print("Null")
t = deque()
t.Enqueue(1)    
t.Enqueue(3)    
t.Enqueue(4)    
t.Enqueue(6)
t.Dequeue()
t.Enqueue_front(2)
t.Enqueue_front(1)
t.Dequeue_rear()
t.Enqueue(5)
t.Enqueue(6)
t.display()    