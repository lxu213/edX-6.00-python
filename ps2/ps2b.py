# july 6, 2014 
# ps2b: paying debt off in a year
# program calculates minimum fixed monthly payment needed in order to pay off debt

# variables contain values from edX
balance = 3926
annualInterestRate = 0.2

year = range(1,13)
monthly_interest_rate = (annualInterestRate) / 12.0
min_pay = 0
curr_balance = balance

while curr_balance > 0:
    curr_balance = balance
    min_pay += 10
    for month in year: 
        monthly_unpaid = curr_balance - min_pay
        curr_balance = monthly_unpaid + (monthly_interest_rate * monthly_unpaid)

print 'Lowest Payment:', min_pay