'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9
Then, the output should be: 11106
'''

digit = input("Enter a digit :  ")
print(int(digit)+int(digit+digit)+int(digit+digit+digit)+int(digit+digit+digit+digit))

