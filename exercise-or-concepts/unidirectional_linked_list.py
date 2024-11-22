class Node:
    data = ""
    next=None
    def __init__(self,data,next) -> None:
        self.data = data
        self.next = next

class LinkedList:
    __head = None
    __tail = None
    def init(self):
        self.__head = Node("firstNode",None)
        
        node_secondNode = Node("secondNode",None)
        self.__head.next = node_secondNode
        
        node_thirdNode = Node("thirdNode",None)
        node_secondNode.next = node_thirdNode
        
        self.__tail = Node("fourthNode",None)
        node_thirdNode.next = self.__tail
        
        return self.__head
    
    def add(self,new_node):
        self.__tail.next = new_node
        self.__tail = new_node
        
    # def insert(self,pos,new_node):
    #     p = self.__head
    #     for i in range(1,pos):
    #         p = p.next
        
            
        
    def output(self,node):
        p = node
        while(p!=None):
            data = p.data
            print(data,"->",end="")
            p = p.next
        print("End")
        
        
        
        
def main():
    linkedlist = LinkedList()
    head = linkedlist.init()
    linkedlist.add(Node("fifthNode",None))
    linkedlist.output(head)
    
if __name__=="__main__":
    main()
    

        
        