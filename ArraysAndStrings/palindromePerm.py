def checkPerm(x):
    dic = {}
    x = x.replace(" ", "").lower()
    for i in x:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if(len(x)%2 == 0):
        for j in dic:
            if dic[j] < 2:
                print("1")
                return False
            elif dic[j]>1 and dic[j]%2 != 0:
                print("11")
                return False
    else:
        singleChar = False
        for j in dic:
            if dic[j]%2 != 0 and not singleChar:
                singleChar = True
            elif dic[j]%2 != 0:
                print("111", j, dic[j])
                return False
    
        
    return True
    

if __name__ == "__main__":
    print('Enter the string:')
    x = input()
    if(checkPerm(x)):
        print('String is Palindrome Permutation')
    else:
        print('Not a palindrome permutation')