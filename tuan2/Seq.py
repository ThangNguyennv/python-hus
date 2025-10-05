def isAlt(a):
    for i in range(0, len(a) - 1):
        if a[i + 1] * a[i] > 0:
            return False
    return True


def isGrow(a):
    for i in range(0, len(a) - 1):
        if a[i + 1] < a[i]:
            return False
    return True


def isMulti(a):
    p = a[1] / a[0]
    for i in range(0, len(a) - 1):
        if (a[i + 1] / a[i]) != p:
            return False
    return True

def isAdd(a):
    p = a[1] - a[0]
    for i in range(1, len(a) - 1):
        if (a[i + 1] - a[i]) != p:
            return False
    return True