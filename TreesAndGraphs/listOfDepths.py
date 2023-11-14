
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.__add_multiple__(values)
            
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __add__(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def __add_multiple__(self, values):
        for i in values:
            self.__add__(i)
            
    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)
    
    def __len__(self):
        num = 0
        for x in self:
            num+= 1
        return num
        
class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        
def create_ll(root):
    if not root:
        return []
    
    curr = root
    fin = [LinkedList([curr])]
    i = 0
    while fin[i]:
        fin.append(LinkedList())
        for node in fin[i]:
            j = node.data
            if j.left:
                fin[i+1].__add__(j.left)
            if j.right:
                fin[i+1].__add__(j.right)
        i += 1
    return fin

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    levels = create_ll(root)
    print(levels[0].head.data.key)
    print(levels[0].head.next)
    print(levels[1].head.data.key)
    print(levels[1].head.next.data.key)
    print(levels[1].head.next.next)
    print(levels[2].head.data.key)
    print(levels[2].head.next.data.key)
    print(levels[2].head.next.next.data.key)
    print(levels[2].head.next.next.next.data.key)
    print(levels[2].head.next.next.next.next)