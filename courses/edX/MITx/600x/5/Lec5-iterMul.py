def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result