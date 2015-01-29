# encoding=utf-8
__author__ = 'bbogle'

'''
L6 PROBLEM 1  (5 points possible)
For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and
put the word 'error' in the box for the value.

Assume we've made the following assignment:
'''

x = (1, 2, (3, 'John', 4), 'Hi')

print x[0]

print x[2]

print x[-1]

print x[2][2]

print x[2][-1]

print x[-1][-1]

#print x[-1][2]

print x[0:1]

print x[0:-1]

print len(x)

print 2 in x

print 3 in x

#print x[0] = 8