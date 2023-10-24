from linkedList import LinkedList

def intersection(a, b):
    first = a.head
    second = b.head
    firstLen = len(a)
    secondLen = len(b)
    diff = abs(firstLen-secondLen)
    if firstLen > secondLen:
        for i in range(diff):
            first = first.next
    elif secondLen > firstLen:
        for i in range(diff):
            second = second.next
    
    while second is not first:
        first = first.next
        second = second.next
    return first
        

if __name__ == "__main__":
    shared = LinkedList()
    shared.__add_multiple__([1, 2, 3, 4])
    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])
    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail
    print(intersection(a, b))