print("Reverse Pyramid Pattern")
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    for space in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(i - 1, 0, -1):
        print("*", end="")
    print()