text = input("Enter your text: ")
if not text:
    print("Text should not be empty")
else:
    count = 0
    for char in text:
        if char.isdigit():
            count += 1

    print(f"The total {count} numbers in text")