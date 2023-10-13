def zeroMatrix(x):
    og = []
    m = len(x)
    n = len(x[0])
    og = [[i for i in row] for row in x]
    for i in range(m):
        for j in range(n):
            if og[i][j] == 0:
                x = makeZero(x, i, j, m, n)
    printMatrix(x, m, n)


def makeZero(x, i, j, m, n):
    for l in range(m):
        x[i][l] = 'x'

    for l in range(n):
        x[l][j] = 'x'
    return x


def printMatrix(x, m, n):
    for i in range(m):
        for j in range(n):
            if x[i][j] == 'x':
                print(0)
            else:
                print(x[i][j])
        print("\n")


if __name__ == "__main__":
    x = [[1, 2, 3, 4, 0],
         [6, 0, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 0, 18, 19, 20],
         [21, 22, 23, 24, 25]]
    

    zeroMatrix(x)
