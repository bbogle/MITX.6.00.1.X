__author__ = 'bbogle'
low = 0
high = 100

print "Please think of a number between 0 and 100! "
while True:
    print "Is your secret number " + str((low+high)/2) + "?"
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",
    print " Enter 'c' to indicate I guessed correctly. ",
    check = raw_input()
    if check == 'h':
        high = (low+high)/2
    elif check == 'l':
        low = (low+high)/2
    elif check == 'c':
        break
    else:
        print "Sorry, I did not understand you input"

print "Game over. Your secret number was:" + str((low+high)/2)