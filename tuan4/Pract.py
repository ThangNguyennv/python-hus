# Hoàn thiện hàm findUniq(a), tìm và trả lại giá trị xuất hiện duy nhất 1 lần trong danh sách a

from collections import Counter

def findUniq(a):
    '''
    Tìm phần tử xuất hiện đúng 1 lần trong danh sách.

    Ví dụ a = [1,2,3,2,3,1,4,5,4] phần tử cần tìm và trả về là 5

    '''
    counter = Counter(a)
    minValue = 99999999
    for key, value in counter.items():
        minValue = min(value, minValue)
    for key, value in counter.items():
        if value == minValue:
            return key
    return None