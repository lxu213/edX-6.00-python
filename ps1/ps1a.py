# june 25, 2014 
# ps1: counting vowels
# script counts the number of vowels contained in a string

# constants
s = 'azcbobobegghakl'
vowel = 'a', 'e', 'i', 'o', 'u'
vowel_count = 0

for n in range(0,len(s)):
    if s[n] == 'a' or s[n] == 'e' or s[n] == 'i' or s[n] == 'o' or s[n] == 'u':
        vowel_count = vowel_count + 1
print vowel_count



# post script comments: strings are iterable 
# for c in s:
# for e in l: (when list = [])
# total += 1