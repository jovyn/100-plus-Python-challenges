'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:

LETTERS 10
DIGITS 3
'''

char_lst =  list(input("Enter a String :"))
digit_count = 0
letter_count = 0

for charac in char_lst:

  if ord(charac) > 64 and ord(charac) < 91:
    letter_count += 1

  elif ord(charac) > 96 and ord(charac) < 123:
    letter_count += 1

  elif ord(charac) > 47 and ord(charac) < 58:
    digit_count += 1

print(f"Letters : {letter_count} and Digits : {digit_count}")