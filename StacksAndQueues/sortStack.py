from stack import Stack

class SortStack:
    def __init__(self):
        self.top = None
        self.s1 = Stack()
        self.s2 = Stack()
        
    def push(self, elem):
        if self.s1.isEmpty() or elem <= self.s1.top.data:
            self.s1.push(elem)
        else:
            while not self.s1.isEmpty() and elem > self.s1.top.data:
                self.s2.push(self.s1.pop())
            self.s1.push(elem)
            while not self.s2.isEmpty():
                self.s1.push(self.s2.pop())
            
            

    def pop(self):
        return self.s1.pop()
        
    def peek(self):
        return self.s1.peek()
    
    def isEmpty(self):
        return self.s1.isEmpty()

if __name__ == "__main__":
    stack = SortStack()
    stack.push(6)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    stack.push(5)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.isEmpty())
    stack.pop()
    print(stack.peek())
    print(stack.isEmpty())