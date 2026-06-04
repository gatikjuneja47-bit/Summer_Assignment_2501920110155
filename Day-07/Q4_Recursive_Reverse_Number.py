print("Recursive Reverse Number")
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse_number(n // 10, rev)
n = int(input("Enter a number: "))
print(reverse_number(n))