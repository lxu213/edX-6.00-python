# july 6, 2014 
# ps2a: paying off credit card debt
# program calculates credit card balance after one year if person only pays minimum

# variables contain values from edX
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

year = range(1,13)
monthly_interest_rate = (annualInterestRate) / 12.0
total_paid = 0

for month in year:
    print 'Month: ', month
    min_monthly_payment = (monthlyPaymentRate)*(balance)
    monthly_unpaid = balance - min_monthly_payment
    balance = monthly_unpaid + (monthly_interest_rate * monthly_unpaid)
    total_paid  += min_monthly_payment
    print 'Minimum monthly payment: ', round(min_monthly_payment,2)
    print 'Remaining balance: ', round(balance,2)
print 'Total paid: ', round(total_paid,2)
print 'Remaining balance:', round(balance,2)