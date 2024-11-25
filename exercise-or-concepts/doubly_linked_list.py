class Node:
    data = ""
    prev = None
    next = None
    def __init__(self,data) -> None:
        self.data = data
        
        
class LinkedList:
    __head = None
    __tail =  None
    
    def init(self):
        self.__head = Node("firstNode")
        self.__head.prev = None
        self.__head.next = None