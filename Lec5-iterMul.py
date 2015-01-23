#encoding=utf-8
__author__ = 'bbogle'

def iterMul(a, b):
    result = 0
    while b>0:
        result +=a
        b -=1
    return result

print iterMul(5,4)