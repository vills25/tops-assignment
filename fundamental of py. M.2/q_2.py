#Write a Python program to get the Factorial number of given number.  

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial_recursive(num)
    print(f"The factorial of {num} is {result}")
