print("Check if a number is an Armstrong number or not")
def is_armstrong(n):
    sum = 0
    order = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        return True
    else:
        return False
n = int(input("Enter a number: "))
if is_armstrong(n):
    print("The number is an Armstrong number")  
else:    
    print("The number is not an Armstrong number")