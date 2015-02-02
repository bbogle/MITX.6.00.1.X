# encoding=utf-8
__author__ = 'bbogle'

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

#FancyDivide([0, 2, 4], 0)

def FancyDivide2(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide2(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"

FancyDivide2([0, 2, 4], 0)