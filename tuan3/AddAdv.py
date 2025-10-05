
# Hoàn thiện hàm addNum(a, b) theo yêu cầu trong đề bài


def addNum(a, b):
    '''
    Cho 2 số nguyên a, b được biểu diễn bởi 2 danh sách
    thực hiện phép cộng 2 số a, b trên 2 danh sách theo quy tắc cộng thông thường. kết quả trả về là 1 danh sách biểu diễn tổng a+b
    ví dụ
    a = [1,2,4,5]
    b =   [7,8,9]

    c = [2,0,3,4]
    '''
    num1 = ''
    num2 = ''
    for x in a:
        num1 += str(x)
    for x in b:
        num2 += str(x)
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    result = str(result)
    m = []
    for c in result:
        m.append(int(c))
    return m