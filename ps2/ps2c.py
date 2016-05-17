# july 13, 2014 
# ps2c: paying debt using bisection search
# program calculates minimum fixed monthly payment needed in order to pay off debt 

# variables contain values from edX
balance = 999999
annualInterestRate = 0.18

year = range(1,13)
epsilon = 0.01
mon_rate = (annualInterestRate) / 12.0
lo = balance / 12.0
hi = (balance * (1 + mon_rate)**12) / 12.0
min_pay = (lo + hi) / 2
curr_balance = 1

while abs(curr_balance) > epsilon:
    curr_balance = balance
    for month in year: 
        monthly_unpaid = curr_balance - min_pay
        curr_balance = monthly_unpaid + (mon_rate * monthly_unpaid)
    if curr_balance > 0:
        lo = min_pay
        min_pay = (lo + hi) / 2
    elif curr_balance < 0:
        hi = min_pay
        min_pay = (lo + hi) / 2
print 'Lowest Payment: ', round(min_pay,2)