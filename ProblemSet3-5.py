# encoding=utf-8
__author__ = 'bbogle'

'''
HANGMAN PART 2: THE GAME  (15 points possible)
Now you will implement the function hangman, which takes one parameter - the secretWord the user is
to guess. This starts up an interactive game of Hangman between the user and the computer.
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and
getAvailableLetters, that you've defined in the previous part.
'''

import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line : string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

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
        if c in lettersGuessed:
            check.append(True)
        else:
            check.append(False)
    if check.count(False) > 0:
        return False
    else:
        return True

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
            result += '_ '
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allChars = string.ascii_lowercase
    for i in lettersGuessed:
        if i in allChars:
            allChars = allChars.replace(i,'')

    return allChars

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = [] # 지금까지 추측한 문자열
    mistakeMade = 0 # 실패 횟수
    availableLetters = string.ascii_lowercase   # 입력 가능한 문자열
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." % (len(secretWord))

    while mistakeMade <9:
        print '-------------'
        if isWordGuessed(secretWord, lettersGuessed):
            print "congratulations, you won!"
            break
        if mistakeMade == 8:
            print "Sorry, you ran out of guesses. The word was %s" % (secretWord)
            break

        print "You have %s guesses left." % (8-mistakeMade)
        print "Available letters: " + availableLetters
        # 입력받은 문자열을 lettersGuessed 에 입력
        tmp = raw_input("Please guess a letter: ").lower()

        # 이미 중복인 경우
        if tmp in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(tmp)
            availableLetters = getAvailableLetters(lettersGuessed)

            # 문자가 들어 있는 경우
            if tmp in secretWord:
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            # 문자가 없는 경우
            else:
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                mistakeMade +=1

hangman('cheetah')
hangman('test')

# harder input cases.
# 1. Testing if we can correctly fill in repeat letters and handle capitalized input ...
# 2. Testing if we handle repeat incorrect guesses...
# 3. Testing if we can correctly guess a word...
# 4. Testing if we run out of guesses...
# 5. Testing if we can correctly fill in multiple letters...
# 6. Testing if we correctly handle repeat guesses...

