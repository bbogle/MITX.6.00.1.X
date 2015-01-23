#encoding=utf-8
__author__ = 'bbogle'

'''
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for
that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is
found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

'''
balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
FixedMonthlyPayment = balance/120 * 10
unpaidBalance = balance
while unpaidBalance > 0:
    print 'start balance: ' + str(balance)

    for i in range(1,13):
        if i == 1:
            previousBalance = balance
        else:
            previousBalance = unpaidBalance

        monthlyUnpaidBalance = previousBalance - FixedMonthlyPayment
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        print '-----------' + str(i) + '--------------'
        print previousBalance,
        print FixedMonthlyPayment,
        print monthlyUnpaidBalance,
        print unpaidBalance

    print 'end balance: ' + str(unpaidBalance)
    if unpaidBalance > 0:
        FixedMonthlyPayment +=10

print FixedMonthlyPayment
'''


balance = 320000
annualInterestRate = 0.2 # 연이율
monthlyInterestRate = annualInterestRate / 12.0 # 월이율
FixedMonthlyPayment = balance/120 * 10 # 고정지불금액
unpaidBalance = balance # 남은금액
while unpaidBalance > 0:
    for i in range(1,13):
        if i == 1:
            previousBalance = balance
        else:
            previousBalance = unpaidBalance
        monthlyUnpaidBalance = previousBalance - FixedMonthlyPayment
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    if unpaidBalance > 0:
        FixedMonthlyPayment +=.1
print 'Lowest Payment: ' + str(FixedMonthlyPayment)
