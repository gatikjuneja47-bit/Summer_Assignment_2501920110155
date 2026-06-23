print("First Non-repeating Character")
string = input("Enter a sentence: ")
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
first_non_repeating_char = None
for char in string:
    if char_freq[char] == 1:
        first_non_repeating_char = char
        break
print("First non-repeating character:", first_non_repeating_char)