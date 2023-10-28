
class QueueNode:
    def __init__(self, data=None, type=None) -> None:
        self.data = data
        self.type = type
        self.next = None
        self.nextCat = None
        self.nextDog = None
    
    def __str__(self) -> str:
        return str(self.data)

class AnimalQueue:
    def __init__(self):
        self.firstCat = None
        self.firstDog = None
        self.lastCat = None
        self.lastDog = None
        self.first = None
        self.last = None
    
    def dequeueAny(self):
        if self.first == None:
            Exception
        else:
            curr = self.first
            self.first = self.first.next
            if(self.first == None):
                self.last = None
            if curr.type == 'Cat':
                # print("1",self.firstCat.next)
                self.firstCat = self.firstCat.nextCat
                if(self.firstCat == None):
                    self.lastCat = None
            else:
                self.firstDog = self.firstDog.nextDog
                if(self.firstDog == None):
                    self.lastDog = None
            
            return curr.data
        
    def dequeueCat(self):
        if self.first == None:
            Exception
        else:
            curr = self.firstCat
            self.first = self.first.next
            if(self.first == None):
                self.last = None
            self.firstCat = self.firstCat.nextCat
            if(self.firstCat == None):
                self.lastCat = None
            
            return curr.data
        
    def dequeueDog(self):
        if self.first == None:
            Exception
        else:
            curr = self.firstDog
            self.first = self.first.next
            if(self.first == None):
                self.last = None
            self.firstDog = self.firstDog.nextDog
            if(self.firstDog == None):
                self.lastDog = None
            
            return curr.data
    
    def enqueue(self, val, type):
        new = QueueNode(val, type)
        
        if(self.last is not None):
            self.last.next = new
        self.last = new
        if(self.first == None):
            self.first = self.last
        if(type == 'Cat'):
            if(self.lastCat is not None):
                self.lastCat.nextCat = new
            self.lastCat = new
            if(self.firstCat == None):
                self.firstCat = self.lastCat
        elif(type == 'Dog'):
            if(self.lastDog is not None):
                self.lastDog.nextDog = new
            self.lastDog = new
            if(self.firstDog == None):
                self.firstDog = self.lastDog
        else:
            raise "Invalid animal"
        
        
            
    def printAll(self):
        print(self.first, self.last, self.firstCat, self.lastCat, self.firstDog, self.lastDog)
        
    def peek(self):
        if self.first == None:
            return "no peek available"
        return self.first.data
    
    def peekDog(self):
        if self.firstDog == None:
            return "no peek available"
        return self.firstDog.data
    
    def peekCat(self):
        if self.firstCat == None:
            return "no peek available"
        return self.firstCat.data
    
    def isEmpty(self):
        return self.first == None
    
    
if __name__ == "__main__":
    queue = AnimalQueue()
    queue.enqueue("Persian", "Cat")
    queue.enqueue("Labrador", "Dog")
    print(queue.peek())
    print(queue.peekCat())
    print(queue.peekDog())
    print(queue.dequeueAny())
    print(queue.peek())
    print(queue.peekCat())
    print(queue.peekDog())
    print(queue.dequeueAny())
    print(queue.peek())
    print(queue.peekCat())
    print(queue.peekDog())

    
            