# encoding=utf-8
__author__ = 'bbogle'

'''
L6 PROBLEM 11  (5 points possible)
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the
entry with the largest number of values associated with it. If there is more than one such entry,
return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'

If there are no values in the dictionary, biggest should return None.
'''

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print animals

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    compNum = 0
    if len(aDict) == 0:
        return None
    for key in aDict.keys():
        if len(aDict[key]) >= compNum:
            biggestKey = key
            compNum = len(aDict[key])
    return biggestKey

#print biggest(animals)
#print biggest({})
#print biggest({'a': [19, 0, 7, 17, 13, 13, 7], 'c': [14, 7, 8, 6], 'b': [17, 6, 3, 4, 6]})
#print biggest({'a': [7, 0, 10, 19, 8, 3, 4, 12, 17], 'c': [14, 0, 3], 'b': [4, 2, 5, 16, 3, 15, 5, 14]})
print biggest({'S': []})