print("Fibonacci Series:")
a, b = 0, 1
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:    print(a, end=' ')
for _ in range(1, n):
        print(b, end=' ')
        a, b = b, a + b