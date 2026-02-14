queue = []
# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))




class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    
    
classQueue = Queue()

classQueue.enqueue(1)
classQueue.enqueue(2)
classQueue.enqueue(3)
classQueue.enqueue(4)
classQueue.enqueue(5)
classQueue.enqueue(6)

classQueue.peek()

classQueue.dequeue()

print("Peek",classQueue.peek())
print("Is empty ?",classQueue.isEmpty())

classQueue.dequeue()
classQueue.dequeue()
classQueue.dequeue()
classQueue.dequeue()
classQueue.dequeue()


print("Is empty? ",classQueue.isEmpty())