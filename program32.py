class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    current=root
    parent=None
    if root is None:
        return Node(data)
    while current is not None:
        parent=current
        if data<current.data:
            current=current.left
        else:
            current=current.right
    if data<parent.data:
        parent.left=Node(data)
    else:
        parent.right=Node(data)
    return root

def nonrecsearch(root,key):
        flag=False
        while root is not None:
            if key==root.data:
                print(f'{key} is present in the BST ')
                flag=True
                break
            elif key<root.data:
                root=root.left
            else:
                root=root.right
        if flag==False:
            print(f'{key} is not present in the BST ')

def recsearch(root,key):
    if root is None:
        print(f'{key} is not present in the BST')
    
    else:
        if key==root.data:
            print(f'{key} is present in the BST')
      
        elif key<root.data:
            return recsearch(root.left,key)
        else:
            return recsearch(root.right,key)
   
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


list=[5,8,6,3,2,7,10,1,4,9]
root=None
for i in list:
    root=insert(root,i)
inorder(root)
print()
# nonrecsearch(root,11)
# nonrecsearch(root,8)

recsearch(root,8)
recsearch(root,12)



