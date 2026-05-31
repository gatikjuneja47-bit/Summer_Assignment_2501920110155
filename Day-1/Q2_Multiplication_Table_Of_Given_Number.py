print("Multiplication Table of a Given Number"
      "\n------------------------------"
      "\nEnter a number: ", end=""
      )
num = int(input())
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")