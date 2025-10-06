n = int(input())
print({x: int(str(x ** 2)[::-1]) for x in range(1, n + 1)})