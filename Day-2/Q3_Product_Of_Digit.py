print("Product of the digits of a number")
number = input("Enter a number: ")
product = 1
for digit in number:
    product *= int(digit)
print("Product of the digits is: ", product)