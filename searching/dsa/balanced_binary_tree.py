class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 0
    
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
        
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
        
        
        
def balanced_bst(sorted_list):
    if not sorted_list:
        return None
    mid = len(sorted_list) // 2
    node = TreeNode(sorted_list[mid])
    node.setLeft(balanced_bst(sorted_list[:mid]))
    node.setRight(balanced_bst(sorted_list[mid+1:]))
    return node

def inorderTraversal(node:TreeNode):
    print(node.getLeft(), node.data, node.getRight()) if node else ""
    return inorderTraversal(node.getLeft()) + [node.data] + inorderTraversal(node.getRight()) if node else []



def insert(node:TreeNode,data):
    if node is None:
        return TreeNode(data)
    if data > node.data:
        node.right = insert(node.getRight(),data)
    elif data < node.data:
        node.left = insert(node.getLeft() ,data)
    else:
        node.count +=1
        
    return node
        
    
node1 = balanced_bst([1,2,3,4,5,7])

insert(node1, 6)

print(inorderTraversal(node1))