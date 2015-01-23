__author__ = "bbogle"

s = 'azcbobobegghakl'
#s = 'abcbcd'
#s = 'hvclvhybi'
#s = 'gbeddljykszojioohnvogyvw'
start = 0
string = ''
check = True
for i in range(len(s)):
    if i == 0:
        string = s[i]
    else:
        if s[i] >= s[i-1]:
            check = True
        else:
            check = False

        if check == True:
            string += s[i]
        else:
            string += ',' + s[i]
lst = string.split(',')
print lst
num = 0
for i in lst:
    #print i
    if num == 0:
        selected = i
    if num > 0:
        #print num,
        #print len(lst[num]),
        #print lst[num]
        if len(lst[num]) > len(selected):
            selected = lst[num]
    num +=1

print selected


# 아비드 하산 풀이
s = 'azcbobobegghakl'
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
