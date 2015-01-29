# encoding=utf-8
__author__ = 'bbogle'
'''
RADIATION EXPOSURE  (25 points possible)
"Radioactive decay" is the process by which an unstable atom loses energy and emits ionizing particles - what is
commonly refered to as radiation. Exposure to radiation can be dangerous and is very important to measure to ensure
that one is not exposed to too terribly much of it.

The radioactivity of a material decreases over time, as the material decays. A radioactive decay curve describes
this decay. The x-axis measures time, and the y-axis measures the amount of activity produced by the radioactive sample.
'Activity' is defined as the rate at which the nuclei within the sample undergo transititions - put simply,
this measures how much radiation is emitted at any one point in time. The measurement of activity is called the Becquerel (Bq).
Here is a sample radioactive decay curve:

'''


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    tot = 0
    while start <stop:
        tot += f(start)*step
        start += step
    return tot

'''
Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 0 - 5.
'''
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

print 'expected : 39.10318784326239'
print radiationExposure(0, 5, 1)
print 'expected : 22.94241041057671'
print radiationExposure(5, 11, 1)

'''
Radium-224.Half-life: 3.66 days. Initial Activity: 400 MBq.
Find total exposure from days 0 - 4.
'''
def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)

print 'expected : 1148.6783342153556'
print radiationExposure(0, 4, 0.25)
print 'expected : 513.4662018628549'
print radiationExposure(5, 10, 0.25)

'''
Uranium-240.Half-life: 14.1 hours. Initial Activity: 200 MBq.
Find total exposure from hours 0 - 3.
'''
def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)

print 'expected : 559.2259707824549'
print radiationExposure(0, 3, 0.1)

'''
Uranium-240.Half-life: 14.1 hours. Initial Activity: 200 MBq.
Find total exposure from hours 48 - 72.
'''
def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)

print 'expected : 523.4527522388149'
print radiationExposure(14, 20, 0.1)