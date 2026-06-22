print("Count of Vowels and Consonants")
string = input("Enter a string: ")
vowels = 0
consonants = 0
for char in string:
    if char.lower() in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Count of vowels is:", vowels)
print("Count of consonants is:", consonants)