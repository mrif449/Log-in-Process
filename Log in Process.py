print("Email/Username/Phone Number:")
username = input()
print("Password:")
password = input()
if username == "tiny.teen12" or username == "01345228795" or username == "tiny.teen12@gmail.com":
    if password == "newpass12@":
        print("Log in Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Email/Username/Phone Number")