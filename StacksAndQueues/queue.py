
class QueueNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class Queue:
    def __init__(self, values=None):
        self.first = None
        self.last = None
        if values is not None:
            self.add_multiple(values)
    
    def remove(self):
        if self.first == None:
            Exception
        else:
            curr = self.first.data
            self.first = self.first.next
            if(self.first == None):
                self.last = None
            return curr
    
    def add(self, val):
        new = QueueNode(val)
        
        if(self.last is not None):
            self.last.next = new
        self.last = new
        if(self.first == None):
            self.first = self.last
            
    
    def peek(self):
        if self.first == None:
            Exception
        return self.first.data
    
    def isEmpty(self):
        return self.first == None
    
    def add_multiple(self, values):
        for x in values:
            self.add(x)
    
if __name__ == "__main__":
    queue = Queue([1,2,3])
    print(queue.peek())
    print(queue.remove())
    print(queue.peek())
    queue.add(7)
    print(queue.peek())
    print(queue.isEmpty())
    
            