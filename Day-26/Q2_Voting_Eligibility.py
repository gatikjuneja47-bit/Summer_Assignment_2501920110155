print("welcome to the voting eligibility checker")
age = int(input("enter your age: "))

if age >= 18:
    print(f"Age: {age} - eligible to vote")
else:
    print(f"Age: {age} - not eligible to vote yet, remaining years: {18 - age}")