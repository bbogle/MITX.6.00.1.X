__author__ = 'bbogle'

'''
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while(abs(ans**2 - x)) >= epsilon and ans <= x :
    ans += step
    numGuesses += 1

print 'numGuesses = ' + str(numGuesses)
if abs(ans**2-x) >= epsilon:
    print 'Failed on square root of ' + str(x)
else:
    print str(ans) + ' is close to the square root of ' + str(x)


x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)

'''

'''
x = 25
epsilon = 0.01
step = 0.01
guess = 0.0
n = 0
while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        print n
        n +=1
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
'''

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0
n = 0
while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        print n
        n +=1
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)