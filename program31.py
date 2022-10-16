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
def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root is None:
        return
    else:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")





list=[5,6,8,3,1,9,2,4,10,7]
root=None
for i in list:
    root=insert(root,i)

inorder(root)
print()
preorder(root)
print()
postorder(root)

