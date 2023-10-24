from linkedList import LinkedList

def checkPalindrome(ll):
    lenLL = len(ll)
    mid=int(lenLL/2)
    isEven = False
    if(lenLL%2 == 0): 
        isEven = True
    i = 0
    stck = []
    curr = ll.head
    isPalindrome = True
    while curr:
        if isEven and i<mid:
            stck.append(curr.data)  
        elif isEven and i>= mid:
            isPalindrome = curr.data == stck.pop()
        elif not isEven and i<(mid):
            stck.append(curr.data)
        elif not isEven and i == (mid):
            i=i
        else:
            isPalindrome = curr.data == stck.pop()
        curr = curr.next
        i += 1
    
    print(isPalindrome)
    

if __name__ == "__main__":
    ll1 = LinkedList([7,1,6,1,7])
    checkPalindrome(ll1)
    ll2 = LinkedList([7,1,1,7])
    checkPalindrome(ll2)
    ll3 = LinkedList([7,1,1,7,5])
    checkPalindrome(ll3)