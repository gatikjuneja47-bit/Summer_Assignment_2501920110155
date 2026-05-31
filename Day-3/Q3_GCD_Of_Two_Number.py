print("GCD of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
smaller = min(a, b)
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        print("GCD is", i)
        break