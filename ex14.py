'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

string_lst = list(input("Enter a Sentence : "))
uc_count = 0
lc_count = 0
for charac in string_lst:
    if ord(charac) > 64 and ord(charac) < 91:
        uc_count += 1
    elif ord(charac) > 96 and ord(charac) < 123:
        lc_count += 1

print(f"Lower case : {lc_count} and Upper case : {uc_count}")