print("Convert Binary to Decimal")
binary_number = input("Enter a binary number: ")
decimal_number = 0
power = 0
for digit in reversed(binary_number):
    if digit == '1':
        decimal_number += 2 ** power
    power += 1
print("Decimal number:", decimal_number)