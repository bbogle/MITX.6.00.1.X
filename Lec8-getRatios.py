# encoding=utf-8
__author__ = 'bbogle'

def getRatios(v1, v2):
    """Assumes : v1 and v2 are lists of equal length of numbers
        Returns a list containing the meaningful values of
            v1[i]/v2[i]"""
    ratios=[]
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NAN = Not a Number
        except:
            raise ValueError('getRatios called with bad arg')
    return ratios



try:
    print getRatios([1.0, 2.0, 7.0, 6.0],
                    [1.0,2.0, 0.0, 3.0])
    print getRatios([],[])
    print getRatios([1.0, 2.0],[3.0])
except ValueError, msg:
    print msg


### compare to traditional code
def getRatios(v1, v2):
    """Assumes: v1 and v2 are lists of equal length of numbers
        ReturnsL a list containing the meaningful values of
        v1[i]/v2[i]"""
    ratios = []
    if len(v1) != len(v2):
        raise ValueError('getRatios called with bad arg')
    for index in range(len(v1)):
        v1Elt = v1[index]
        v2Elt = v2[index]
        if (type(v1Elt) not in (int, float))\
            or (type(v2Elt) not in (int, float)):
            raise ValueError('getRatios called with bad arg')
        if v2Elt == 0.0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else:
            ratios.append(v1Elt/v2Elt))
    return ratios