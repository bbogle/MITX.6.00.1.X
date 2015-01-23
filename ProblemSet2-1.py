#-*-coding: utf-8 -*-
__author__ = 'bbogle'

'''
A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 4842
balance = 320000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
for i in range(1, 13):
    previousBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    minimumMonthlyPayment = 29157.09
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

    print 'Month: ' + str(round(i,2)),
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2)),
    print 'Remaining balance: ' + str(round(balance,2))

    if i==12:
        RemainingBalance = balance

    totalPaid += minimumMonthlyPayment

print "Total paid: " + str(round(totalPaid,2)),
print "Remaining balace: " + str(round(RemainingBalance,2))