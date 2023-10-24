from linkedList import LinkedList

def checkLoop(ll):
    slow = ll.head
    fast = ll.head.next
    
    while slow is not fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

if __name__ == "__main__":
    ll = LinkedList([1,2,3,4,5])
    loop_node = ll.head.next.next
    ll.tail.next = loop_node
    print(checkLoop(ll))
    print(checkLoop(LinkedList([1,2,3,4,5])))