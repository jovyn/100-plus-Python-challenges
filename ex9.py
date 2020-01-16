'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

lines = []
while True:
    input_string = input("Enter some long string or press ENTER to quit: ")
    if len(input_string) == 0:
        break
    else:
        lines.append(input_string)

for line in lines:
    print(str(line).upper())




