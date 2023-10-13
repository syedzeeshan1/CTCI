def rotateMatrix(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            x[i][j], x[j][i] = x[j][i], x[i][j]
    for i in range(len(x)):
        x[i] = x[i][::-1]
            
    printMatrix(x)
    
def printMatrix(x):
    for i in range(len(x)):
        for j in range(len(x)):
            print(x[i][j])
        print("\n")

if __name__ == "__main__":
    print('Enter the string:')
    x = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    
    # [[00,01,02], 
    #  [10,11,12], 
    #  [20,21,22]]
    
    # [[20,10,00], 
    #  [21,11,01], 
    #  [22,12,02]]
    rotateMatrix(x)