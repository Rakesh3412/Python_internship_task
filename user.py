email = input("Enter your email : ")

username = email.split("@")[0]

if username.isidentifier():
    print("Valid email username")
else:
    print("Invalid email username")