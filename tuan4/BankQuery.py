def solve():
    m = []
    while True:
        key = input().strip()
        if key == '':
            break
        m.append(key)
    result = 0
    for x in m:
        key = x.split(' ')[0]
        value = x.split(' ')[1]
        if key == 'D':
            result += int(value)
        elif key == 'W':
            result -= int(value)
    return result
print(solve())
