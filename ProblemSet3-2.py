# encoding=utf-8
__author__ = 'bbogle'

'''
HANGMAN PART 1: IS THE WORD GUESSED?
'''

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    check = []
    for c in secretWord:
        #print c
        if c in lettersGuessed:
            #print True
            check.append(True)
        else:
            #print False
            check.append(False)
    #print check
    if check.count(False) > 0:
        return False
    else:
        return True


# print isWordGuessed(secretWord, lettersGuessed)
print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
#print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
#print isWordGuessed('carrot', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't'])
#print isWordGuessed('tact', ['a'])