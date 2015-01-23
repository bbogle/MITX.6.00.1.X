__author__ = "bbogle"

s = 'azcbobobegghak'

cnt = 0
for c in s:
    if c == 'a' or c=='e' or c=='i' or c=='o' or c=='u':
        cnt +=1

print "Number of vowles: " + str(cnt)


cnt = 0
lst = ['a','e','i','o','u']
for c in s:
    if c in lst:
        cnt +=1
print "Number of vowles: " +str(cnt)



