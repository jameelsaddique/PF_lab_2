import re
# we always import the re module to match method and match match the our input to the patterns
# This pattern ensures a standard structure: local@domain.extension
regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
# it contain small alphabats and capital letter and numeric value from 0-9  and . dot for .com .ly etc and import for @ 
Email = input("Enter your Email: ")
if not Email:
    print("Email cannot be empty")
elif re.match(regex, Email):
    print("Valid Email")
else:
    print("Invalid Email address")