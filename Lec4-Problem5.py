__author__ = 'bbogle'

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    #print min(max(x,lo),hi)
    #print max(lo,min(x,hi))
    print min(max(lo,x),hi),
    print min(max(x,lo),hi),
    print min(max(lo,hi),x),
    print max(min(x,hi),lo),
    print max(min(hi,x),lo),
    print max(x,min(lo,hi)),
    print max(lo,min(hi,x))

clip(-9.0, 3.69, 2.0)
clip(2.15, 4.25, 6.0)
clip(4.69, -3.23, 4.75)