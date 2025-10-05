# Hoàn thiện hàm customSort


def customSort(a):
    '''
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    '''
    chan = []
    le = []
    for x in a:
        if x % 2 == 0:
            chan.append(x)
        else:
            le.append(x)
    result = []
    chan.sort()
    le.sort(reverse=True)
    for x in chan:
        result.append(x)
    for x in le:
        result.append(x)
    return result
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(customSort(a))