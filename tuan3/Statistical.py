import math
def mean(s):
    return sum(s) / len(s)

def variance(s):
    result = sum((float(c) - mean(s)) ** 2 for c in s)
    return result / len(s)

def standarddeviation(s):
    return math.sqrt(variance(s))
