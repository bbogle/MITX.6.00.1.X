__author__ = 'bbogle'

# lecture 3.6, slide 2
# bisection search for square root

x = 24
epsilon = 0.16
numGuess = 0
low = 0.0
high = x

ans = (high+low)/2.0
while abs(ans**2-x) >= epsilon:
    print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuess +=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print ('numGuess = ' + str(numGuess))
print (str(ans) + ' is close to square root of ' + str(x))

