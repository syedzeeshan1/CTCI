
class StackNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class Stack:
    def __init__(self, values=None):
        self.top = StackNode()
        if values is not None:
            self.add_multiple(values)
    
    def pop(self):
        if self.top == None:
            Exception
        else:
            curr = self.top.data
            self.top = self.top.next
            return curr
    
    def push(self, val):
        new = StackNode(val)
        new.next = self.top
        self.top = new
    
    def peek(self):
        if self.top == None:
            Exception
        return self.top.data
    
    def isEmpty(self):
        return self.top.data == None
    
    def add_multiple(self, values):
        for x in values:
            self.push(x)
    
if __name__ == "__main__":
    stack = Stack([1,2,3])
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    stack.push(7)
    print(stack.peek())
    print(stack.isEmpty())
    
            