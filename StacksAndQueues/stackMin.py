
class StackNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prevMin = None
    
    def __str__(self) -> str:
        return str(self.data)

class Stack:
    def __init__(self, values=None):
        self.top = StackNode()
        self.mini = self.top.data
        if values is not None:
            self.add_multiple(values)
    
    def pop(self):
        if self.top == None:
            Exception
        else:
            curr = self.top.data
            if curr == self.mini:
                self.mini = self.top.prevMin
            self.top = self.top.next
            return curr
    
    def push(self, val):
        new = StackNode(val)
        if self.mini == None or val < self.mini:
            new.prevMin = self.mini
            self.mini = new.data
            
        new.next = self.top
        self.top = new
    
    def peek(self):
        if self.top == None:
            Exception
        return self.top.data
    
    def min(self):
        if self.mini == None:
            Exception
        return self.mini
    
    def isEmpty(self):
        return self.top == None
    
    def add_multiple(self, values):
        for x in values:
            self.push(x)
    
if __name__ == "__main__":
    stack = Stack([2,3,1])
    print(stack.min())
    # print(stack.peek())
    stack.pop()
    # print(stack.peek())
    print(stack.min())
    stack.push(0)
    # print(stack.peek())
    print(stack.min())
    stack.pop()
    print(stack.min())
    print(stack.isEmpty())
    
            