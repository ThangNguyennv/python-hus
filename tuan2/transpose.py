def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        row = list(map(int, line.split('\t')))
        m.append(row)
    return m


def transpose(m):
    a = len(m)
    b = len(m[0])
    t = [[0 for j in range(0, a)] for i in range(0, b)]
    for i in range(0, a):
        for j in range(0, b):
            t[j][i] = m[i][j]
    return t


def printMatrix(t):
    for i in range(0, len(t)):
        for j in range(0, len(t[i])):
            print(t[i][j], end="\t")
        print()

m = inputMatrix()
t = transpose(m)
printMatrix(t)
