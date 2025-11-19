class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        
        #sentinal head and tail
        self.head = Node("head", "head")
        self.tail = Node("tail","tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            
            self._remove(node)
            self.add(node)
            return node.value
        return -1
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]
            
    def display_rank(self):
        node = self.head.next
        
        print("---------------")
        print(self.head.key, self.head.value, end=" <-> ")
        while node:
            print(node.key,node.value, end=" <-> ")
            node = node.next
        print("---------------")
        print(self.cache)
            
            
lru = LRUCache(5)
lru.put(0,0)
lru.put(1,1)
lru.put(2,2)
lru.put(3,3)
lru.put(4,4)
lru.put(5,5)
lru.put(6,6)

print(lru.get(0))
lru.display_rank()
    