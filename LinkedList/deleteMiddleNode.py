from linkedList import LinkedList

def deleteMiddleNode(middle):
    middle.data = middle.next.data
    middle.next = middle.next.next
    
        
    

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.__add_multiple__([1,2,3])
    middle = linkedList.__add__(4)
    linkedList.__add_multiple__([5,6,7,8])
    print("linkedlist initial = ")
    print(linkedList)
    print("-----------")
    deleteMiddleNode(middle)
    print(linkedList)