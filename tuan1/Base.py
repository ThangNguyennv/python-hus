import math
def isPerfectNumber(number: int):
    """
    Số hoàn hảo là một số nguyên dương mà tổng các ước nguyên dương thực sự của nó
    (các ước nguyên dương ngoại trừ chính số đó) bằng chính nó. Hoàn thiện hàm isPerfectNumber(number)
    nhận vào số nguyên dương number và trả về True nếu number là số hoàn hảo
    và False nếu number không phải là số hoàn hảo.

    Ví dụ:
    input: 6
    ouput: True

    input: 14
    output: False
    """
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return number == sum


def drawPatterm(height: int):
    """
    Hãy vẽ hình vuông có chiều cao height.
    Ví dụ
    input: 4
    output:
    ****
    *  *
    *  *
    ****
    """
    for row in range(1, height + 1):
        print("*", end="")
    print()
    for row in range(2, height):
        for col in range(1, height + 1):
            if col == 1 or col == height:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for row in range(1, height + 1):
        print("*", end="")


def caculateExp(x: float, n: int):
    """
    Hoàn thiện hàm tính e^x theo công thức đã cho của đề bài.
    Ví dụ:
    input: 2 100 (Tương ứng x = 2 và n = 100)
    output: 7.3890561
    """
    return math.e ** x



