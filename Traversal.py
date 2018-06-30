
# coding: utf-8

# In[ ]:

###tree traversal implementation----
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#--binary tree class        
class BinaryTree:
    def __init__(self,value):`
        self.root=Node(value) 
        
    #--display traversal---
    def print_traversal(self,traversalType):
        if(traversalType=='preorder'):
            return self.preorder(tree.root)
        if(traversalType=='inorder'):
            return self.inorder(tree.root)
        
        if(traversalType=='postorder'):
            return self.postorder(tree.root)
    #--preorder-----
    def preorder(self,start,traversal=''):
        if start:
            traversal+=str(start.data)+'->'
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    #---inorder------
    def inorder(self,start,traversal=''):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=str(start.data)+'-'
            traversal=self.inorder(start.right,traversal)
        return traversal  
    #---postorde------
    def postorder(self,start,traversal=''):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=str(start.data)+'-'
        return traversal
    

#--make binary tree----        
        
tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(6)
tree.root.right.left=Node(7)
tree.root.right.right=Node(8)

#call traversal method----
print (tree.print_traversal('preorder'))
print (tree.print_traversal('inorder'))
tree.print_traversal('postorder')

