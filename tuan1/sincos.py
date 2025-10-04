def sinTaylor(x):
    sk = x
    sin = sk
    numTerms = 20
    for i in range(2, numTerms):
        sk = (sk * (-1) * x * x) / ((2 * i - 1) * (2 * i - 2))
        sin = sin + sk
    return sin

def cosTaylor(x):
    sk = 1
    cos = sk
    numTerms = 20
    for i in range(1, numTerms):
        sk = (sk * (-1) * x * x) / ((2 * i) * (2 * i - 1))
        cos = cos + sk
    return cos