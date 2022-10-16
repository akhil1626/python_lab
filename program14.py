class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
       
class ll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    #insert at end
    def atend(self,data):
        new_node=Node(data)
        self.size+=1
        if self.head is None:
            self.head=self.tail=new_node
            return
        
        self.tail.next=new_node
        self.tail=new_node

    #printlist
    def print(self):
        if self.head is None:
            print("list is empty")
            return

        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None") 
    #delete 
    def delete(self,val):
        if self.head is None:
            print("there are is no data to  be delete")
            return
        if self.head==val:
            if self.head==self.tail:
                self.head=self.tail=None
                self.size-=1
                return
            else:
                self.head=self.head.next
                self.size-=1
                return
        temp=self.head
        while(temp!=self.tail and temp.next.data!=val):
            temp=temp.next
        if temp==self.tail:
            print("element not found")
            return
        if temp.next == self.tail:
            temp.next = None
            self.tail = temp
            return
        temp.next=temp.next.next 
        self.size-=1
        
            
        
      
     # get size
    def getSize(self):
        print("\nthe size of the list is ",self.size)   
   
list=ll()
for i in range(1,7):
    list.atend(i)
list.print() 
list.delete(6)
list.print()
list.getSize()




    
