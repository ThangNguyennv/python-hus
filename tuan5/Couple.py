def isCheckReverse(s):
    return s[::-1]

def findCouple(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.readlines()
        result = []
        for line in data:
            for ch in line.strip().split(' '):
                result.append(ch)
        k = []
        for i in range(0, len(result)):
            if isCheckReverse(result[i]) in result:
                k.append(result[i])
                k.append(isCheckReverse(result[i]))
                break
        m = sorted(k)
        return (m[0], m[1])
    return 'None','None'