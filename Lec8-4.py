# encoding=utf-8
__author__ = 'bbogle'

def avg(grades, weights):
    assert not len(grades) == 0, 'no grades data'
    newgr = [convertLetterGrade(elt) for elt in grades]
    return dotProduct(newgr, weights)/len(newgr)

def avg(grades, weights):
    assert not len(grades) == 0, 'no grades data'
    assert len(grades) == len(weights), 'wrong number grades'
    newgr = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgr, weights)/len(newgr)
    assert 0.0 <= result <= 100.0
    return result


