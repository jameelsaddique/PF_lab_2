words = input("Enter words separated by space: ").split()

if not words:
    print("No words provided")

else:
    sentence = " ".join(words)

    print("Generated Sentence:", sentence)
    