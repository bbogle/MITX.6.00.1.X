# encoding=utf-8
__author__ = 'bbogle'

'''
PRINTING OUT ALL AVAILABLE LETTERS  (5 points possible)
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters,
lettersGuessed. This function returns a string that is comprised of lowercase English letters - all
lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getAvailableLetters(lettersGuessed)
abcdfghjlmnoqtuvwxyz
'''

import string

def getAvailableLetters(lettersGuessed):
    allChars = string.ascii_lowercase
    for i in lettersGuessed:
        if i in allChars:
            allChars = allChars.replace(i,'')

    return allChars


print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
print getAvailableLetters([])
print getAvailableLetters(['b', 'x', 's', 'q', 'u', 'v', 'h', 'f', 'o', 'y', 'd', 'g'])
print getAvailableLetters(['y', 'z', 'l', 'g', 't'])
print getAvailableLetters(['c', 'a', 'y', 'p', 'r'])