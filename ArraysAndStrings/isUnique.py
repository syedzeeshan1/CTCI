
def checkUnique(stri):
    dic = {}
    for s in stri:
        if s in dic:
            return False
        dic[s] = 1
        
    return True

if __name__ == "__main__":
    print('Enter the string:')
    x = input()
    if(checkUnique(x)):
        print('string has unique chars')
    else:
        print('string has duplicate chars')
        

