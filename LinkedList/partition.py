from linkedList import LinkedList

def createPartition(ll, x):
    lower = LinkedList()
    higher = LinkedList()
    curr = ll.head
    while curr:
        if int(curr.data) < x:
            lower.__add__(curr.data)
        else:
            higher.__add__(curr.data)
        curr = curr.next
    lower.tail.next = higher.head
    return lower

if __name__ == "__main__":
    linkedList = LinkedList([3,5,8,5,10,2,1])
    x = 5
    print(createPartition(linkedList, x))
    