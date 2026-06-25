print("Common Characters in Strings")
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

common_characters = set(str1) & set(str2)
if common_characters:
    print("Common characters:", ", ".join(common_characters))
else:
    print("No common characters found.")