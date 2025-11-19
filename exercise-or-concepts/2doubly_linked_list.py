class Node:
    data = ""
    prev = None
    next = None
    def __init__(self,data) -> None:
        self.data = data
        
    def addNext(self, node):
        self.next = node
    def addPrev(self, node):
        self.prev = node
        
        
class LinkedList:
    __head = None
    __tail =  None
    
    def __init__(self):
        self.__head = Node("firstNode")
        self.__head.prev = None
        self.__head.next = None
        
        self.__tail = Node("TailNode")
        self.__tail.prev = self.__head
        self.__tail.next = None
        
        self.__head.next = self.__tail
        
        
    def add(self,new_node):
        new_node.next = self.__head.next
        self.__head.next.prev = new_node
        self.__head.next = new_node
        
    def remove(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.__head.next = node.next
        if node.next:
            node.next.prev = node.prev
    def display(self):
        curr = self.__head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")
        
        
node1 = Node("first")
node2 = Node("second")
node3 = Node("third")
node4 = Node("four")
node5 = Node("five")
node6 = Node("six")

Linkedlst = LinkedList()
Linkedlst.add(node1)
Linkedlst.add(node2)
Linkedlst.add(node3)
Linkedlst.add(node4)
Linkedlst.add(node5)
Linkedlst.add(node6)
Linkedlst.remove(node5)

Linkedlst.display()
