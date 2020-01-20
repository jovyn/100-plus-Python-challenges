'''
Enter email and password and return if its compliant or not.
'''

import re

email_in = input("Enter your Email:")
passwd_in = input("Enter your password:")

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
passwd_pattern = re.compile(r"(^[a-zA-Z0-9#@%&*!$]{8,32}$)")

if email_pattern.search(email_in):
    print(f"Email ID : {email_in}  is Complaint ")

else:
    print("Enter a proper Email Id")


if passwd_pattern.search(passwd_in):
    print(f"Password : {passwd_in}  is Complaint ")

else:
    print("Enter a proper Password")