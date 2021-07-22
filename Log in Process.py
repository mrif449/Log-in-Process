usrnm = "tiny.teen12"
email = "tiny.teen12@gmail.com"
phone = "01345228795"
pswd = "newpass12@"
print("Username/Email/Phone Number:")
username = input()
print("Password:")
password = input()
if (username == usrnm or username == email or username == phone) and password == pswd:
    print("Log in Successful")
elif (username != usrnm or username != email or username != phone) or password != pswd:
    if (username != usrnm or username != email or username != phone) and password == pswd:
        print("Incorrect Email/Username/Phone Number")
    elif (username == usrnm or username == email or username == phone) and password != pswd:
        print("Incorrect Password")
    else:
        print("Invalid Account")
