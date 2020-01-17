'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

'''
def CheckEven(lst):
  chk_all_even = []
  for n in lst:
     if int(n) % 2 == 0:
       chk_all_even.append(0)
     else:
       chk_all_even.append(1)
  return(chk_all_even)

ans = []
s = ","

for num in range(1000, 30001):
  lst = list(str(num))
  test = [0,0,0,0]
  if (CheckEven(lst)) == test:
    ans.append(str(num))

print(s.join(ans))