def input_array():
    array = list(map(int, input().split()))
    return array

def find_second_max_min(array):
    a = -99999999  # second_max
    b = 99999999  # second_min
    tempMax = -999999
    tempMin = 999999
    for i in range(len(array)):
        tempMax = max(array[i], tempMax)
    for i in range(len(array)):
        tempMin = min(array[i], tempMin)
    for i in range(len(array)):
        if array[i] < tempMax:
            a = max(array[i], a)
    for i in range(len(array)):
        if array[i] > tempMin:
            b = min(array[i], b)
    return b, a


array = input_array()
print(find_second_max_min(array))