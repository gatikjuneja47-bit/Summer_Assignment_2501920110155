print("Count Words in a Sentence")
sentence = input("Enter a sentence: ")
words = 1
for char in sentence:
    if char == " ":
        words += 1
print(f"Number of words in the sentence: {words}")   