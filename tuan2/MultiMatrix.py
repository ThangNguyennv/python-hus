import numpy as np

def inputMatrix():
    rows, cols = map(int, input().split())
    m = []
    for i in range(0, rows):
        row = list(map(int, input().split()))
        m.append(row)
    return m


def multiMatrix(m1, m2):
    r = []
    r = np.dot(m1, m2)
    return r


def printMatrix(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            print(m[i][j], end=" ")
        print()


m1 = inputMatrix()
m2 = inputMatrix()

mm = multiMatrix(m1, m2)
printMatrix(mm)