print("Count Set Bits in a Number")
number = int(input("Enter a number: "))
count = 0
while number:
    count += number & 1
    number >>= 1
print("Number of set bits:", count)