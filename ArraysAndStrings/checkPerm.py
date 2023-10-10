def isPerm(x, y):
    dic = {}
    dic2 = {}
    if len(x) != len(y):
        return False
    for i in x:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    for j in y:
        if j in dic2:
            dic2[j] = dic2[j]+1
        else:
            dic2[j] = 1
    for z in dic:
        if z not in dic2:
            return False
        elif dic[z] != dic2[z]:
            return False
    
    return True
            

if __name__ == "__main__":
    print('Enter the first string:')
    x = input()
    print('Enter the second string:')
    y = input()
    if(isPerm(x,y)):
        print('input strings are permutations of each other')
    else:
        print('not permutated')