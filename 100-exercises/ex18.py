'''
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example: If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be: ABd1234@1
'''
print("Enter comma seperated passwords to check fro compliance : ")
print("Eg.  password1,password2,....etc")
print("Program will return passwords that are compliant with the criteria")
#s = ","
input_str = input()
pass_lst = (input_str.split(","))

def isCompliant(password_str):
    is_uc = False  #is UpperCase
    is_lc = False  #is LowerCase
    is_num = False #is Number
    is_splchar = False #is special character

    str_to_check = list(password_str)
    for ch in str_to_check:
        if  (ord(ch) >= 33) and (ord(ch)<= 47): # in ascii range (33,47) Check for Sp Chars
            is_splchar = True

        elif (ord(ch) >= 58) and (ord(ch) <= 64): # in ascii range (58,65) Check for Sp Chars
            is_splchar = True

        elif (ord(ch) >= 91) and (ord(ch) <= 96): # in ascii range (91,96) Check for Sp Chars
            is_splchar = True

        elif (ord(ch) >= 123) and (ord(ch) <=126): # in ascii range (123,126) Check for Sp Chars
            is_splchar = True

        elif (ord(ch) >= 48) and (ord(ch) <= 57):
            is_num = True

        elif (ord(ch) >= 65) and (ord(ch) <= 90):
            is_uc = True

        elif (ord(ch) >= 97) and (ord(ch) <= 122):
            is_lc = True

        else:
            pass

    if is_splchar and is_num and is_lc and is_uc:
        return 1
    else:
        return 0


for pass_item in pass_lst:
    pass_item = pass_item.strip()

    if isCompliant(pass_item):
        print(f"The passcode {pass_item} is compliant")
    else:
        print(f"{pass_item} is NOT Compliant. Try Again")



