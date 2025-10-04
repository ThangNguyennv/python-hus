import math
def sqrt_newton(c):
    EPSILON = 1e-15
    t = c
    if t == c / t:
        return math.sqrt(c)
    else:
        while math.fabs(t - c / t) < (EPSILON * t):
            t = (t + (c / t)) / 2
    return math.sqrt(t)