class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
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
            t.previous = self.rear
            self.rear = t
            self.size+=1
    def Enqueue_front(self,elem):
        t = Node(elem)
        if self.front == None:
            self.front = self.rear = t
            self.size+=1
        else:
            
            self.front.previous = t
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
            print("the Queue is now empty...")
            return delv
        else:
            delv = self.front.data
            self.front = self.front.next
            self.front.previous = None
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
            itr = self.front
            while itr.next!= self.rear:
                itr = itr.next
            delv = self.rear.data
            itr.next = None
            self.rear = itr
            self.size-=1
    def display(self):
        temp=self.front
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.next
        
    def display_Rev(self):
        itr = self.rear
        while itr!=None:
            print(itr.data,end = " ")
            itr = itr.previous
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
print()
t.display_Rev()   