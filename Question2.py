import re

password = input("Enter your password: ")

# Regex pattern
pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'

if not password:
    print("Password cannot be empty")

elif re.match(pattern, password):
    print("✅ Strong Password")

else:
    print("❌ Weak Password")
    print("Password must contain:")
    print("- At least one uppercase letter")
    print("- At least one number")
    print("- At least one special character (@$!%*?&)")