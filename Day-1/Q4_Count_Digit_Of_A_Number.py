print("Count of Digits in a Number"
      "\nEnter a number: ", end=""
      )
num = int(input())
count = 0
while num != 0:
    num //= 10
    count += 1
print(f"Count of digits in the number is {count}")