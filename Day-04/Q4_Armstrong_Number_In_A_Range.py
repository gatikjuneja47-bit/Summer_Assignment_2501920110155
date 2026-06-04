print("Armstrong Numbers in a Range:")
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    if num == sum_of_digits:
        print(num, end=" ")
