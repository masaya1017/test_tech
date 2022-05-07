
# 単純な計算
def add(x, y):
    return x+y


def substract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):

    if y == 0:
        raise ZeroDivisionError('0では割り切れません')

    return x // y
