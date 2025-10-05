def isMagicSquare(m):
    n = len(m)
    if n == 0:
        return False

    magic_sum = sum(m[0])

    for row in m:
        if sum(row) != magic_sum:
            return False

    for col in range(n):
        if sum(m[row][col] for row in range(n)) != magic_sum:
            return False

    diag_main = sum(m[i][i] for i in range(n))
    diag_secondary = sum(m[i][n - i - 1] for i in range(n))

    if diag_main != magic_sum or diag_secondary != magic_sum:
        return False
    return True


def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        row = list(map(int, line.split('\t')))
        m.append(row)
    return m

