import math

a = [0] * 1000001
def sang():
    for i in range(1, 1000001):
        a[i] = i
    for i in range(2, int(math.sqrt(1000000 + 1))):
        if a[i] == i:
            for j in range(i * i, 1000001, i):
                if a[j] == j:
                    a[j] = i

def parse(n):
    sang()
    result = []
    temp = n
    while n != 1:
        n = int(n)
        result.append(a[n])
        n /= a[n]
    print(temp, "=", " x ".join(map(str, result)))

parse(60)


