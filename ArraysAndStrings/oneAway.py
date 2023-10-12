def checkOneReplace(x, y):
    onePass = False
    for idx, char in enumerate(x):
        if onePass and char != y[idx]:
            return False
        elif char != y[idx]:
            onePass = True
    return True

def checkOneInsert(x, y):
    for idx, char in enumerate(x):
        if (x[:idx] + x[idx + 1:]) == y:
            return True
            
    return False

def checkOneAway(x, y):
    if(len(x) == len(y)):
        return checkOneReplace(x, y)
    elif(len(x)+1 == len(y)):
        return checkOneInsert(y, x)
    elif(len(x) == len(y)+1):
        return checkOneInsert(x, y)
    return False
    
if __name__ == "__main__":
    print('Enter the first string:')
    x = input()
    print('Enter the second string:')
    y = input()
    if(checkOneAway(x, y)):
        print('String is One Away')
    else:
        print('Not a One Away')