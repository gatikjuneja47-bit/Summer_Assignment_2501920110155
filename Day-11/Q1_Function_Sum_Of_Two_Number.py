print("Sum of two numbers")
def sum_of_two_numbers(num1, num2):
    return num1 + num2
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
result = sum_of_two_numbers(number1, number2)
print("The sum of", number1, "and", number2, "is:", result)