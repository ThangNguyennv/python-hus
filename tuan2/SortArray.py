def inputArray():
    array = list(map(int, input().split()))
    return array


def sort_array(array):
    r = []
    r = sorted(array)
    return r


def printArray(r):
    print(' '.join(map(str, r)))


arr = inputArray()
r = sort_array(arr)
printArray(r)