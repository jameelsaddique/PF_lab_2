name = input("Enter your name: ")

if not name:
    print("Name cannot be empty")

else:
    formatted_name = name.strip().title()

    print("Formatted Name:", formatted_name)