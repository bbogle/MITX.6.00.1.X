__author__ = 'bbogle'

# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 0.00000000001
y = 90.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))

# sqrt(24) = 4.898979846