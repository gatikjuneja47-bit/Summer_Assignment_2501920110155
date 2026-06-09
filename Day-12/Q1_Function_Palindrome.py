print("Check if a number is a palindrome or not")
def is_palindrome(n):
    if n == n[::-1]:
        #string slicing to reverse the string and compare with original string
        return True
    else:
        return False
n = input("Enter a number: ")
if is_palindrome(n):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")