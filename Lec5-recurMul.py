#encoding=utf-8
__author__ = 'bbogle'

def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

print recurMul(5,4)