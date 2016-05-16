# june 25, 2014 
# ps1: counting bobs
# script prints the number of times the string 'bob occurs in s

s = 'azcbobobegghakl'
total = 0

for n in range(0,len(s)-2):
    if s[n] == 'b' and s[n+1] == 'o' and s[n+2] == 'b':
        total+=1
print('Number of times bob occurs is: ' + str(total))