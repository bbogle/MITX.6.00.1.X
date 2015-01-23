__author__ = "bbogle"

s = "azcbobobegghakl"
s = 'veoboobboobobbbobob'
cnt = 0
for i in range(len(s)):
    if i+3 <= len(s):
        #print s[i:i+3:]
        #print s[i:i+3:]
        if s[i:i+3:] == 'bob':
            cnt += 1
print "Number of times bob occurs is: " + str(cnt)

