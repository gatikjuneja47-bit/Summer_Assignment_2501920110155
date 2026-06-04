print("Strong Number")
num = int(input("Enter a number: "))
temp = num
sum_of_factorials = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    temp //= 10
if sum_of_factorials == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")