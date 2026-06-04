print("LCM of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
larger = max(a, b)
for i in range(larger, a * b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM is", i)
        break