print("Largest Prime Factor")
num = int(input("Enter a number: "))
num1 = num
largest_prime_factor = 1
i = 2
while i * i <= num:
    if num % i == 0:
        largest_prime_factor = i
        while num % i == 0:
            num //= i
    i += 1
if num > 1:
    largest_prime_factor = num
print(f"The largest prime factor of {num1} is {largest_prime_factor}.")