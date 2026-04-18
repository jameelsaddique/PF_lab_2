text = input("Enter your text: ")

bad_words = ["badword", "hate", "stupid"]

if not text:
    print("Input cannot be empty")

else:
    cleaned_text = text

    for word in bad_words:
        cleaned_text = cleaned_text.replace(word, "***")
        cleaned_text = cleaned_text.replace(word.upper(), "***")
        cleaned_text = cleaned_text.replace(word.capitalize(), "***")

    print("Filtered Text:", cleaned_text)