print("Sum of the digits of a number")
number = input("Enter a number: ")
number = int(number)
sum_of_digits = 0
while number > 0:
        sum_of_digits += number % 10
        number //= 10
print("Sum of the digits is: ", sum_of_digits)