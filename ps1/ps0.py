# june 25, 2014 
# fibonacci
# function returns the nth fibonacci number

def fib(n):
    if n == 1: 
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
while True:
    x = int(raw_input('Enter n: '))
    print('The ' + str(x) + 'th fibonacci number is ' + str(fib(x)))