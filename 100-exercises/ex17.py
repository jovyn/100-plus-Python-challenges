'''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500
'''

tr_log = []
count = 0
print("Enter transaction logs. D -Deposit, W - withdrawal and Enter  to quit : ")
while True:
    console_log = input()
    if len(console_log) == 0:
        break
    else:
        tr_log.append(console_log)

for item in tr_log:
    x = item.split()
    if ord(x[0]) == 68:
        count = count + int(x[1])
    elif ord(x[0]) == 87:
        count = count - int(x[1])
    else:
        pass

print(f"Balance is : {count}")