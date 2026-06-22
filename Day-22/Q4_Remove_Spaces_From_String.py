print("Remove Spaces from a String")
string = input("Enter a string: ")
for char in string:
    if char == " ":
        string = string.replace(" ", "")
print(f"String after removing spaces: {string}")