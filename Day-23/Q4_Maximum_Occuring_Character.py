print("Maximum Occurring Character")
string = input("Enter a sentence: ")
char_freq = {}
for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
max_char = None
max_freq = 0
max_char != " "
for char, freq in char_freq.items():
    if freq > max_freq:
        max_freq = freq
        max_char = char
print(f"Maximum occurring character: {max_char} and its frequency: {max_freq}")