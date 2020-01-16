#Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


num_seq = input("Enter comma seperated numbers as input: ")
num_list = num_seq.split(",")
num_tuple = tuple(num_list)
print(f"List : {num_list}")
print("---------------------")
print(f"Tuple : {num_tuple}")