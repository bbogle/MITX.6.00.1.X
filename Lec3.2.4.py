__author__ = 'bbogle'

# Find the cube root of a perfect cube

x = int(raw_input("Enter a number : "))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x :
    print (str(x) + ' is not a perfect cube')
else:
    print ("Cube root of " + str(x) + ' is ' + str(ans))

