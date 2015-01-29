# encoding=utf-8
__author__ = 'bbogle'

'''
L6 PROBLEM 7A  (1/1 point)
Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

Assume that

testList = [1, -4, 8, -9]

Example Question:

>>> print testList
[5, -20, 40, -45]
Solution to Example Question
  >>> print testList
  [1, 4, 8, 9]
'''

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

>>> print testList
  [1, 4, 8, 9]

# Your Code Here
def absApply(a):
    if a < 0:
        return a * -1
    else:
        return a

applyToEach(testList, absApply)

  >>> print testList
  [2, -3, 9, -8]

# Your Code Here
def plusOne(a):
    return a + 1

applyToEach(testList, plusOne)

  >>> print testList
  [1, 16, 64, 81]

# Your Code Here
def square(a):
    return a*a
applyToEach(testList, square)