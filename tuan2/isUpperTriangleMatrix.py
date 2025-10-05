def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        row = list(map(int, line.split('\t')))
        m.append(row)
    return m

def isUpperTriangleMatrix(m):
    for i in range(1, len(m)):
        for j in range(0, i):
            if m[i][j] != 0:
                return False
    return True


m = inputMatrix()
print(isUpperTriangleMatrix(m))