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
        
    def insert(self,pos,new_node):
        p = self.__head
        i = 0
        while p.next != None and i < pos-1:
            p = p.next
            i+=1
        new_node.next = p.next
        p.next = new_node
        
    def remove(self,pos):
        p = self.__head
        i = 0
        remove_node = p.next
        while (p.next != None and i < pos):
            p = p.next
            remove_node = p.next
            i+=1
        p.next = remove_node.next
        
            
        
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
    # linkedlist.insert(2,Node("addedNode",None))
    linkedlist.remove(1)
    linkedlist.output(head)
    
if __name__=="__main__":
    main()
    

        
        