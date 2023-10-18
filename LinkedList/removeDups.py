from linkedList import LinkedList

def removeDuplicates(linkedList):
    curr = linkedList.head
    previous = None
    nonDupSet = set()
    while curr:
        if curr.data in nonDupSet:
             previous.next = curr.next
        else:
            nonDupSet.add(curr.data)
            previous = curr
            
        curr = curr.next
    linkedList.tail = previous
    print(linkedList)
    
def removeDuplicatesBetter(linkedList):
    curr = linkedList.head
    rabbit = linkedList.head
    while curr:
        rabbit = curr
        while rabbit.next:
            if rabbit.next.data == curr.data:
                rabbit.next = rabbit.next.next
            else:
                rabbit = rabbit.next
        curr = curr.next
    linkedList.tail = rabbit
    
    print("-----follow up----")
    print(linkedList)
            
    

if __name__ == "__main__":
    
    linkedList = LinkedList.generate(100, 0, 9)
    print("linkedlist initial = ")
    print(linkedList)
    print("-----------")
    removeDuplicates(linkedList)
    linkedList = LinkedList.generate(100, 0, 9)
    print("linkedlist initial = ")
    print(linkedList)
    removeDuplicatesBetter(linkedList)