from linkedList import LinkedList

def kthToLast(ll, k):
    totalLen = ll.__len__()
    pos = totalLen-k
    i = 0
    for x in ll:
        if i == pos-1:
            return x
        else:
            i += 1

def approachTwo(ll, k):
    curr = second = ll.head
    count = 0
    while curr:
        if count > k:
            second = second.next
        curr = curr.next
        count+=1
    return second
            

if __name__ == "__main__":
    print("enter k")
    k = int(input())
    linkedList = LinkedList.generate(100, 0, 9)
    print("linkedlist initial = ")
    print(linkedList)
    print("-----------")
    print(kthToLast(linkedList, k))
    linkedList = LinkedList.generate(10, 0, 9)
    print("linkedlist initial = ")
    print(linkedList)
    print("-----------")
    print(approachTwo(linkedList, k))