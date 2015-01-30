# encoding=utf-8
__author__ = 'bbogle'

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)

print rem(2,5)
print rem(5,5)
print rem(7,5)