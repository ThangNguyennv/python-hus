# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.

import math
def solver(f, a, b, e=0.000001):
    if f(a) * f(b) > 0:
        return None
    while True:
        c = (a + b) / 2
        if math.fabs(f(c)) <= e:
            return c
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
