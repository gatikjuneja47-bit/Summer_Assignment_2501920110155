print("Reverse of String")
string = input("Enter a string: ")
reverse = ""
for char in string:
    reverse = char + reverse
print("Reverse of the string is:", reverse)