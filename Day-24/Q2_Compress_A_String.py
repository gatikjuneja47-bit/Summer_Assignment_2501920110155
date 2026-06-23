print("String Compression")
string = input("Enter the string to compress: ")
copmressed_string = ""
count = 1
current_char = string[0]
for i in range(1,len(string)):
    if string[i] == current_char:
        count += 1
    else:
        copmressed_string += current_char
        current_char = string[i]
        count = 1
copmressed_string += current_char
print("Compressed string:", copmressed_string)