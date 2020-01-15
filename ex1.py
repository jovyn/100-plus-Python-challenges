#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

num_list = []
for num in range(2000, 3200):    #range(start, stop, step)
    if num % 2 == 0 and num % 5 != 0:
        #print(num)
        num_list.append(num)
#print(num_list) # prints list
num_string = ','.join(map(str, num_list)) #using map to converts numbers to str
print(f"Answer: {num_string}")
