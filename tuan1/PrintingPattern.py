def leftHalfPyramid(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end="")
        print()

def rightHalfPyramid(n):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if col <= n - row:
                print(" ", end="")
            else:
                print("*", end="")
        print()

def fullPyramid(n):
    for row in range(1, n + 1):
        for col in range(1, n - row + 1):
            print(" ", end="")
        for col in range(1, 2 * row):
            print("*", end="")
        print()

def invertedFullPyramid(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(" ", end="")
        for col in range(1, 2 * (n - row + 1)):
            print("*", end="")
        print()

def hollowPyramid(n):
    for row in range(1, n + 1):
        for col in range(1, n - row + 1):
            print(" ", end="")
        for col in range(1, 2 * row):
            if col == 1 or col == 2 * row - 1 or row == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

leftHalfPyramid(5)
print()
rightHalfPyramid(5)
print()
fullPyramid(5)
print()
invertedFullPyramid(5)
print()
hollowPyramid(5)