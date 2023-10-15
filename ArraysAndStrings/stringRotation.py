def isRotation(x, y):
    m = len(x)
    n = len(y)
    if(m!=n):
        return False
    for i in range(n):
        if isSubstring(x, y[:i]):
            temp = len(y[i:])
            if x[:temp] == y[i:]:
                
                return True
    return False        

def isSubstring(x, y):
    substrLen = len(y)
    for i in range(len(x)):
        if x[i: substrLen] == y:
            return True
        elif substrLen > len(x):
            return False
        i = i+1
        substrLen = substrLen+1
    return False
            

if __name__ == "__main__":
    print('Enter the first string:')
    x = input()
    print('Enter the second string:')
    y = input()
    
    print(isRotation(x, y))
    