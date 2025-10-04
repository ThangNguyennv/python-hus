# Hoàn thiện hàm fibonacciSeries(n) nhận vào số nguyên dương n và in ra n số đầu tiên của dãy Fibonacci.

count = 3

def fibo(a, b, n):
    global count
    if count < n:
        fn = a + b
        print(fn, end=" ")
        a = b
        b = fn
        count += 1
        fibo(a, b, n)
    else:
        print(a + b)


def displayFibonacciSeries(n):
    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, 1, end="")
        return
    if n >= 2:
        print(1, 1, end=" ")
        fibo(1, 1, n)