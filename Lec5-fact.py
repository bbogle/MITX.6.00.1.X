# encoding=utf-8
__author__ = 'bbogle'

def factI(n):
    """
    n: assumes that n is an int > 0
    :return: n!
    """
    res = 1
    while n>1:
        res = res * n
        n -=1
    return res

def factR(n):
    """
    n: assumes that n is an int > 0
    :return: n!
    """
    if n ==1:
        return n
    return n*factR(n-1)

print factI(5)
print factR(5)