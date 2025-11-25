class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def setLeft(self,left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
        
root = TreeNode("root")
nodea = TreeNode('a')
nodeb = TreeNode('b')
nodec = TreeNode('c')
noded = TreeNode('d')
nodee = TreeNode('e')
nodef = TreeNode('f')
nodeg = TreeNode('g')

root.setLeft(nodea) 
root.setRight(nodeb)
nodea.setLeft(nodec)
nodea.setRight(noded)
nodeb.setLeft(nodee)
nodeb.setRight(nodef)

nodec.setLeft(nodeg)



# verify binary tree

def isBinaryTree(node):
    if node is None:
        return True
    if hasattr(node, "left") and hasattr(node, "right"):
        return isBinaryTree(node.left) and isBinaryTree(node.right)
    return False

print("Binary tree?", isBinaryTree(root))


# traverse the tree
def Traverse(node):
    if node:
        Traverse(node.left)
        print(node.data, " ")
        Traverse(node.right)
        
Traverse(root)