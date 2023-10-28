from stack import Stack

class TwoStackQueue:
    def __init__(self):
        self.top = None
        self.s1 = Stack()
        self.s2 = Stack()
        self.shifted = False
        
    def add(self, elem):
        if not self.shifted:
            self.s1.push(elem)
        else:
            self.shift_elems()
            self.shifted = False
            self.s1.push(elem)
            
    def shift_elems(self):
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())

    def remove(self):
        if self.shifted:
            return self.s2.pop()
        else:
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            elem = self.s2.pop()
            self.shifted = True
            return elem
        
    def peek(self):
        if self.shifted:
            return self.s2.peek()
        else:
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            self.shifted = True
            elem = self.s2.peek()
            return elem
    
    def isEmpty(self):
        if self.shifted:
            self.shift_elems()
            self.shifted = False
        return self.s1.isEmpty()
        
        
if __name__ == "__main__":
    queue = TwoStackQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.peek())
    print(queue.remove())
    print(queue.peek())
    queue.add(7)
    print(queue.peek())
    print(queue.isEmpty())
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print(queue.isEmpty())