user_input = input("Enter your text: ")

# Remove leading and trailing spaces
cleaned_input = user_input.strip()

if not user_input:
    print("Input cannot be empty")

elif cleaned_input == "":
    print("Input contains only spaces")

else:
    print("Original Input:", user_input)
    print("Cleaned Input:", cleaned_input)