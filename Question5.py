text = input("Enter your sentence: ")
keyWord = input("Which keyword you want to find: ")
if not text and not keyWord:
    print("Text and keyword cannot be empty")
elif keyWord in text:
    print(f"{keyWord} found in text ")
else:
    print("Keyword not found")
