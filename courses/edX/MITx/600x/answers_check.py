def gcdIter(a, b):
    gdc = min(a, b)
    while gdc > 0:
        if a % gdc == 0 and b % gdc == 0:
            break
        else:
            gdc -= 1
    return gdc


def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def iterLen(x):
    length = 0
    for _ in x:
        length += 1
    return length


def recurLen(x):
    characters = 0
    if x == '':
        return 0
    else:
        characters += 1
        return characters + recurLen(x[1:])