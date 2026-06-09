print("Check if a number is a perfect number or not")
def is_perfect(n):
    sum_of_divisors = 0 
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

n = int(input("Enter a number: "))
if is_perfect(n):
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")

