import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n + 1))):
        if n % i == 0:
            return False
    return True

def sumNumber(n):
    n = str(n)
    result = sum(int(x) for x in n)
    return result

def isLuckyNumber(n):
    return isPrime(n) and (sumNumber(n) % 5 == 0)

def findLuckyNumber(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            for ch in line.split(' '):
                if ch.isdigit():
                    ch = int(ch)
                    if isLuckyNumber(ch):
                        return ch
    return 0