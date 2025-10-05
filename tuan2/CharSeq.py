from collections import Counter
def solve(s):
    count = Counter(s)
    maxChar = ''
    maxFreg = -999999999999
    for char, freq in count.items():
        maxFreg = max(maxFreg, freq)
    for char, freq in count.items():
        if freq == maxFreg:
            maxChar = char
    print(maxChar, maxFreg)

solve(input())