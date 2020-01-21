'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

'''

# Taken from the solution set :(

i,j = map(int, input("Enter2 nos i,j : ").split(","))
some_lst = []

for n1 in range(i):
  tmp = []
  for n2 in range(j):
    tmp.append(n1*n2)
  some_lst.append(tmp)

print(some_lst)