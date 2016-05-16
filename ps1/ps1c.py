# june 26, 2014
# ps1: alphabetical substrings
# script prints the longest substring of s in which the letters occur in alphabetical order

import string
alphabet = string.ascii_lowercase 
s = 'azcbobobegghakl'
alph_loc = 0
best_so_far = []
current_string = []
            
for i in range(len(s)):
    c = s[i]
    print 'c in string:', c
    for letter in alphabet:
        print 'letter in alph: ', letter
        if c == letter:
            current_string.append(c)
            print 'current_string', current_string
            break
        else:
            if i == 0:
                pass
            elif alphabet.index(s[i]) < alphabet.index(s[i-1]):
                print 's[i]', s[i]
                print 's[i-1]', s[i-1]
                if len(current_string) > len(best_so_far):
                    print 'hi'
                    print 'current_string', current_string
                    best_so_far = current_string
                current_string = []
                print "****: best_so_far:", best_so_far
                    
print 'longest substring = ', best_so_far   
          
                    
# else cases:
# first/base case
# last/base case

# separate thing: always be updating best_so_far (after 