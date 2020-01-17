'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
'''

num_lst = input("Enter a sequence of nos. comma separated:  ")
num_lst = num_lst.split(",")

new_lst = [ str(int(n)*int(n)) for n in num_lst if int(n) % 2 != 0 ]
s = ","
print(s.join(new_lst))



