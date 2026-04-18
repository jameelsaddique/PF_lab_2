import re
username = input("Enter your user Name: ")
patterns = r'^[A-Za-z0-9]+$'
if not  username:
    print("userName cannot be empty")
else:
    if re.match(patterns,username):
        print(f"Valid User Name {username}")
    else:
        print("Invalid Username")
