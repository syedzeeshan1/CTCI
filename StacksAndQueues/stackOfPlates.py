from stack import Stack

class StackPlates:
    def __init__(self, threshold) -> None:
        self.threshold = threshold
        self.stacks = []
        self.sizes = []
        
    def getTopOfLastStack(self):
        
        if not self.isEmpty():
            pointer = len(self.stacks)-1
            return self.stacks[pointer].peek()
        else:
            return -1
    
    def getLastStackIndex(self):
        if not self.isEmpty():
            return len(self.stacks)-1
        else:
            return -1
        
    def isEmpty(self):
        return len(self.stacks) == 0
    
    def push(self, elem):
        index = self.getLastStackIndex()
        
        if index == -1:
            newStack = Stack([elem])
            self.stacks.append(newStack)
            self.sizes.append(1)
        elif self.sizes[index]+1 <= self.threshold:

            self.stacks[index].push(elem)
            self.sizes[index] += 1
        else:

            newStack = Stack([elem])
            self.stacks.append(newStack)
            self.sizes.append(1)
        print(self.sizes)
    
    def pop(self):
        index = self.getLastStackIndex()
        if index != -1:
            if self.sizes[index] == 1:
                self.stacks.pop()
                self.sizes.pop()
            else:
                data = self.stacks[index].pop()
                self.sizes[index] -= 1
                return data
            print(self.sizes)
        else:
            raise "empty error"
    
    def popAt(self, index):
        if index >= 0 and index < len(self.stacks):
            if self.sizes[index] == 1:
                self.stacks.remove(self.stacks[index])
                self.sizes.remove(self.sizes[index])
            else:
                data = self.stacks[index].pop()
                self.sizes[index] -= 1
                print(self.sizes)
                return data
            
        else:
            raise "err"
            

if __name__ == "__main__":
    stack = StackPlates(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.getTopOfLastStack())
    stack.pop()
    print(stack.getTopOfLastStack())
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.popAt(1))