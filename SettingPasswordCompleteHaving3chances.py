import re
user_name = input("Enter your username:: ")
x = True
attempt = 0
while x:

    p = input("Enter your password:: ")

    attempt += 1

    if len(p) < 8 or len(p) > 16:
        print("The length of the password should be atleast 8-16 characters..")
        # break
    if user_name in p:
        print("The username should not be part of password!!")
        # break
    if not re.search("[a-z]", p):
        print("The password should contain some alphabets!!")
        # break
    if not re.search("[A-Z]", p):
        print("The password should contain some Caps!!")
        # break
    if not re.search("[0-9]", p):
        print("The password should contain numbers!!")
        # break
    if not re.search("[!@#$%]", p):
        print("The password should contain some special characters!!")
        # break
        print("The password is not valid:Attempts remaining:: ", 3 - attempt)
        print("\n")

    else:
        print("The password is valid!!")
        break
        # x = False
    if attempt >= 3:
        exit("Attempt Exceeded!!")
