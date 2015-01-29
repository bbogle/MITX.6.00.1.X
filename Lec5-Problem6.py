# encoding=utf-8
__author__ = 'bbogle'

'''
L5 PROBLEM 6  (5 points possible)
Although Python provides a built-in function for computing the length of a string, we can write our own.

Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the
number of characters in the string.
'''

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    cnt = 0
    for i in aStr:
        cnt +=1
    return cnt

print lenIter('abc')