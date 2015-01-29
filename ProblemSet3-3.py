# encoding=utf-8
__author__ = 'bbogle'
'''
PRINTING OUT THE USER'S GUESS  (5 points possible)
Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters,
lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in
lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getGuessedWord(secretWord, lettersGuessed)
'_ pp_ e'
'''


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for c in secretWord:
        #print c
        if c in lettersGuessed:
            result += c
        else:
            result += '_'
    return result

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)
print getGuessedWord('pineapple', ['q', 'y', 'o', 'h', 'b', 'f', 't', 'z', 'w', 'g'])
print getGuessedWord('broccoli', ['j', 'c', 'u', 'm', 'y', 'w', 's', 'q', 'r', 'i'])