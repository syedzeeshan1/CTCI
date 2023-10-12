def doCompression(x):
    ogLen = len(x)
    finString = ''
    currCount = 1
    for idx, char in enumerate(x):
        if idx == 0:
            pass
        elif idx == len(x)-1 and char != x[idx-1]:
            finString = finString + x[idx-1] + str(currCount) + char + '1'
        elif idx == len(x)-1:
            finString = finString + x[idx-1] + str(currCount+1)
        elif char == x[idx-1]:
            currCount += 1
        elif char != x[idx-1]:
            finString = finString + x[idx-1] + str(currCount)
            currCount = 1
    if len(finString) >= ogLen:
        print(x)
    else:
        print(finString)

if __name__ == "__main__":
    print('Enter the string:')
    x = input()
    doCompression(x)