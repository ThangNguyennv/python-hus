def multiNum(a, b):  # a, b là kiểu list
    number = int("".join(map(str, a)))
    k = []
    m = []
    for x in b:
        k.append((x * number))

    for i in range(len(k) - 1, -1, -1):
        m.append(str(k[i]) + "0" * (len(k) - i - 1))
    result = sum(int(c) for c in m)
    l = []
    for x in str(result):
        l.append(int(x))
    return l