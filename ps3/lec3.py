# lecture 3 problem 9
# bisection search
# july 5, 2014

print 'Please think of a number between 0 and 100!'
low = 0
high = 100
compy_guess = (low + high)/2
user_input = 0

while user_input != 'c':
    print 'Is your secret number ' + str(compy_guess) + '?'
    user_input = raw_input('Enter "h" to indicate the guess is too high. ' + \
                                    'Enter "l" to inicate the guess is too low. ' + \
                                    'Enter "c" to inicate that I guessed correctly. ')
    if user_input == 'h':
        high = compy_guess
        compy_guess = (low + high)/2
    elif user_input == 'l':
        low = compy_guess
        compy_guess = (low + high)/2
    elif user_input == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.' 
    
print 'Game over. Your secret number was: ' + str(compy_guess)