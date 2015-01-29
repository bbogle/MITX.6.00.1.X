# encoding=utf-8
__author__ = 'bbogle'

'''
L5 PROBLEM 10  (5 points possible)
Ben Bitdiddle tried to implement fibMetered with global variables, to count the number of recursive calls needed for
each Fibonacci number calculated. But he made a mistake in using the global variable! Examine his code below carefully
and then answer the questions:
어디가 잘못되었는지 찾아보시오.
'''

def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):

        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)