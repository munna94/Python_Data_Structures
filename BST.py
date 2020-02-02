class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        newNode=Node(value)
        
        if self.root is None:
            self.root=newNode
        else:
            currentNode=self.root
            while(True):
                if(value<currentNode.value):
                    if(currentNode.left is None):
                        currentNode.left=newNode
                        break
                    else:
                        currentNode=currentNode.left
                else:
                    if(currentNode.right is None):
                        currentNode.right=newNode;
                        break
                    else:
                        currentNode=currentNode.right
                        
    def lookup(self, node,value):
        if (node is None):
            return False
        currentNode=self.root
        while(currentNode is not None):
            if(currentNode.value is value):
                return True#if match then return true
            elif(value<currentNode.value):
                    currentNode=currentNode.left#if value is less than the current node means we should track left side
            elif(value>currentNode.value):
                currentNode=currentNode.right#if value is greater than the current node means we should track right side
        return False
                
                        
    
    def traverse(self,node,traversal=''):
        traversal+=str(node.value)+'->'
        if node.left is not None: 
            traversal=  self.traverse(node.left,traversal)#consider this method is defind somewhere and it taking traversal 
            #parameter and returning after concate traversal so we need to reinitialize the latest return to traversal
            #if we will not reinitalize then it will take old traversal value and then it will proceed further
        if node.right is not None:
            traversal=self.traverse(node.right,traversal)
        return traversal
    
        
        

bst=BST()
bst.insert(20)
bst.insert(10)
bst.insert(50)
bst.insert(90)
bst.insert(70)
val=bst.traverse(bst.root)
print(val.rstrip('->'))#remove end wala ->
print(bst.lookup(bst.root,70))
