print("welcome to the number guessing game")
import random
numberA = int(input("enter a number: "))
number = random.randint(1,10)
print(number)

if number==numberA:
    print("you WONNN")
else:
    print("you lose\nTRY AGAIN") 