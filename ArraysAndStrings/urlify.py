def urlify(x, n):
    print("Method 1:")
    x = x[:n].replace(" ", "%20")
    print(x)

def urlify2(x, n):
    print("Method 2:")
    listedChars = list(x)
    idx = len(listedChars)
    
    for i in reversed(range(n)):
        if listedChars[i] == " ":
            listedChars[idx - 3: idx] = "%20"
            idx = idx - 3
        else:
            listedChars[idx-1] = listedChars[i]
            idx = idx - 1
            
    print("".join(listedChars[idx:]))

if __name__ == "__main__":
    print('Enter the string:')
    x = input()
    print('Enter the lenght:')
    y = int(input())
    urlify(x, y)
    urlify2(x, y)