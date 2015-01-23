def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        return True
    elif char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        return True
    else:
        return False

##print isVowel('o')
##print isVowel('F')
##print isVowel('i')
##print isVowel('U')

def isVowel2(char):
    vowel=['a','e','i','o','u']
    if char in vowel:
        return True
    else:
        return False

print isVowel2('o')
print isVowel2('F')
print isVowel2('i')
print isVowel2('U')

def isVowel3(char):
    if char.lower() in 'aeiou':
        return True
    else:
        return False
