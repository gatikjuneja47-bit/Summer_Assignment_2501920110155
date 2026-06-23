print("Removing Duplicate Characters in a String")
string = input("Enter the string: ")
result = ""
for char in string:
    if char not in result:
        result += char
print(f"String after removing duplicates: {result}")