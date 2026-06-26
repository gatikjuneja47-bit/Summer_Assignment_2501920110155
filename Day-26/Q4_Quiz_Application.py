print("Welcome to the Quiz")
score = 0
print("Answer the following questions:")
question1 = input("What is the capital of India? \n ")
if question1.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is New Delhi.")

question2 = input("What is the currency of the United States? \n ")
if question2.lower() == "dollar":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Dollar.")

question3 = input("What is the largest planet in our solar system? \n ")
if question3.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Jupiter.")

print("Your final score is:", score)
if score == 3:
    print("Excellent! You got all the answers right!")