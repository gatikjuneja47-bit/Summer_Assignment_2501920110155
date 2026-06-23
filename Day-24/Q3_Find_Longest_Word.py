print("Longest Word in a String")
string = input("Enter the string: ")
words = 1
for char in string:
    if char == " ":
        words += 1
longest_word = ""
current_word = ""
for char in string:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = "" 
if len(current_word) > len(longest_word):
    longest_word = current_word
print(f"Longest word in the string: {longest_word}")