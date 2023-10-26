
class ThreeStackArray:
    def __init__(self, size, number):
        self.size = size
        self.number = number
        self.array = [0]*size*number
        self.sizes = [0]*number
        
        
    def indexOfTop(self, num):
        return (num * self.size) + self.sizes[num]
    
    def push(self, num, elem):
        if not self.isFull(num):
            self.array[self.indexOfTop(num)] = elem
            self.sizes[num] += 1
            
        else:
            raise "Error"
    
    def pop(self, num):
        if not self.isEmpty(num):
            
            val = self.array[self.indexOfTop(num)]
            self.array[self.indexOfTop(num)] = 0
            self.sizes[num] -= 1
            return val
        else:
            raise "Error"
    
    def peek(self, num):
        if not self.isEmpty(num):
            return self.array[self.indexOfTop(num)]
        else:
            raise "Error"
    
    def isEmpty(self, num):
        return self.sizes[num] == 0
    
    def isFull(self, num):
        return self.sizes[num] == self.size 

if __name__=="__main__":

    new = ThreeStackArray(size=3,number=3)
    print(new.isEmpty(0))
    new.push(0, 1)
    new.push(0, 2)
    new.push(1, 4)
    new.push(1, 5)
    new.push(2, 7)
    new.push(2, 8)
    print(new.peek(0), new.peek(1), new.peek(2))
    new.pop(0)
    new.pop(1)
    new.pop(2)
    print(new.peek(0), new.peek(1), new.peek(2))
    