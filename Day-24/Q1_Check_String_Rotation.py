print("Check String Rotation")
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1
if is_rotation(str1, str2):
    print("The strings are rotations of each other.")
else:    print("The strings are not rotations of each other.")