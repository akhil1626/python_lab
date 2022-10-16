class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
        


    # insertion
    def insert(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=self.tail=new_node
            return
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            return
    # deletion
    def delete(self,val):
        if self.head is None:
            print("list is empty bro.....!")
            return
        if self.head.data==val:
            if self.head==self.tail:
                self.head=self.tail=None
                return
            else:
                self.head=self.head.next
                self.head.prev=None
                return

        temp=self.head
        while(temp.next.data!=val and temp!=None):
            temp=temp.next
        if temp==None:
            print("element not found")
            return
        if temp.next==self.tail:
            temp.next=None
            self.tail=temp
            return
        temp.next=temp.next.next
        temp.next.prev=temp

    def print(self):
        if self.head is None:
            print("list is empty bro......!")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def size(self):
        return self.size
d=dll()
for i in range(1,12):
    d.insert(i)
d.print()
d.delete(21)
d.print()
# 1print("the list has",d.size(),"elements")




    
    