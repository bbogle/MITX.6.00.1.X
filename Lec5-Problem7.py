# encoding=utf-8
__author__ = 'bbogle'
'''
L5 PROBLEM 7  (5 points possible)
For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string),
by counting up the number of characters in the string.

Hint: String slicing may be useful in this problem...
'''
def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr!='':
        return 1 + lenRecur(aStr[1:])
    else:
        return 0
print lenRecur('bnwbsdezeykfi')