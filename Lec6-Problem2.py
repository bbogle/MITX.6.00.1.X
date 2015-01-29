# encoding=utf-8
__author__ = 'bbogle'

'''
L6 PROBLEM 2  (5 points possible)
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other
element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    #print len(aTup)
    rst = ()
    for i in range(len(aTup)):
        #print aTup[i]
        if i%2 == 0:
            rst = rst + (aTup[i],)
    return rst

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
print oddTuples(())
print oddTuples((9,))
print oddTuples((13, 12, 0, 12, 10, 17, 7))
print oddTuples((2, 9, 0, 8, 3, 13, 20))
print oddTuples((18, 20, 6, 0, 17, 0, 13, 0))
print oddTuples((17, 6, 7, 7, 20))
print oddTuples((7, 3, 17, 14, 13, 14, 2, 9, 11))


'''
another solution 1
'''
def oddTuples2(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

'''
another solution 2
'''
def oddTuples3(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]