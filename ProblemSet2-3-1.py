#encoding=utf-8
__author__ = 'bbogle'

import time
start_time = time.clock()

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLowerbound = balance/12
monthlyPaymentUpperbound = (balance * (1+monthlyInterestRate)**12)/12.0

#expectLowestPayment = 29157.09
low = monthlyPaymentLowerbound
high = monthlyPaymentUpperbound
epsilon = 0.01

def searchLowestPayment(low, high, total):
    ans = (low+high)/2.0
    for i in range(1,13):
        #남은금액
        if i == 1:
            unpaidBalance = total
            previousBalance = total
        else:
            previousBalance = unpaidBalance

        monthlyUnpaidBalance = previousBalance - ans
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if i == 12:
            if abs(unpaidBalance) > epsilon:
                if unpaidBalance < 0:
                    high = ans
                    searchLowestPayment(low,high,total)
                elif unpaidBalance > 0:
                    low = ans
                    searchLowestPayment(low,high,total)
            else:
                print 'Lowest Payment: ' + str(round(high,2))
                break

searchLowestPayment(low,high, balance)


print time.clock() - start_time, "sec"