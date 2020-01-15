# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num = 8
factorial = 1
i = 1
while num >= i:
    factorial = factorial * i
    i = i + 1

print(factorial)
