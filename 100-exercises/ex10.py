'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
'''

input_str = input("Enter a Sentence: ")
input_str = list(set(input_str.split(" ")))
input_str.sort()
#print(input_str)
str_val = ""
for item in input_str:
    str_val = str_val + str(item) + " "

print(str_val)



