from linkedList import LinkedList

def addSum(ll1, ll2):
    finalRes = LinkedList()
    carryOver = 0
    curr1 = ll1.head
    curr2 = ll2.head
    summation(curr1, curr2, carryOver, finalRes)
    print(finalRes)
    
    
def add(val1, val2, carryOver):
    return val1+val2+carryOver  

def summation(first, second, carryOver, finalRes):
    if not first and not second:
        if carryOver != 0:
            finalRes.__add__(str(carryOver))
        return finalRes
    elif not first:
        sum = add(0, second.data, carryOver)
        if(sum > 9):
            finalRes.__add__(str(sum)[1])
            carryOver = int(str(sum)[0])
        else:
            finalRes.__add__(str(sum))
            carryOver = 0
        return summation(first, second.next, carryOver, finalRes)
    elif not second:
        sum = add(first.data, 0, carryOver)
        if(sum > 9):
            finalRes.__add__(str(sum)[1])
            carryOver = int(str(sum)[0])
        else:
            finalRes.__add__(str(sum))
            carryOver = 0
        return summation(first.next, second, carryOver, finalRes)
    else:
        sum = add(first.data, second.data, carryOver)
        if(sum > 9):
            finalRes.__add__(str(sum)[1])
            carryOver = int(str(sum)[0])
        else:
            finalRes.__add__(str(sum))
            carryOver = 0
        return summation(first.next, second.next, carryOver, finalRes)
      

if __name__ == "__main__":
    ll1 = LinkedList([7,1,6])
    ll2 = LinkedList([5,9,2])
    addSum(ll1, ll2)
    ll1 = LinkedList([7,1,6,5])
    ll2 = LinkedList([5,9])
    addSum(ll1, ll2)
    ll1 = LinkedList([9,9,9])
    ll2 = LinkedList([1])
    addSum(ll1, ll2)
    ll1 = LinkedList([9,7,8])
    ll2 = LinkedList([6,8,5])
    addSum(ll1, ll2)