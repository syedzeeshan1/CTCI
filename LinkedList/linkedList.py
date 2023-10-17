import random

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
    
    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))