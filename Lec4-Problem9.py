__author__ = 'bbogle'

def odd(x):
    '''
    x: int or float
    :return: True if x is odd, False otherwise
    '''
    # Your code here
    return min(True, max(False,x%2))

def odd2(x):
    return x%2 == 1

print odd(2)
print odd(3)
print odd2(2)
print odd2(3)

