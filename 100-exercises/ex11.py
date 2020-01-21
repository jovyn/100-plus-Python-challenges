'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

nos = input("Enter binary nos comma seperated : ")
nos_lst = nos.split(",")
deci_lst = []  # List for all decimal values
deci_lst2 = []  # List of decimals divisible by 5

for num in nos_lst:
    num = num[::-1]  # reverse the binary string
    digits = list(num)
    i = 0
    lst = []
    # deci_lst = []
    for d in digits:
        # print(f"digit - {d}")
        val = (2 ** i) * int(d)
        lst.append(val)
        # print(val)
        i = i + 1
    deci = sum(lst)
    deci_lst.append(deci)
    if deci % 5 == 0:
        deci_lst2.append(deci)

print(f"Decimal values are : {deci_lst}")
print(f"Decimal values divisible by 5 are : {deci_lst2}")