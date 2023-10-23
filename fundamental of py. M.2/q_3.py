#Write a Python program to get the Fibonacci series of given range. 

# Input from the user
range_limit = int(input("Enter the range for the Fibonacci series: "))

if range_limit < 0:
    print("Please enter a non-negative number.")
else:
    first = 0
    second = 1
    print("Fibonacci series up to", range_limit, ": ", end="")

    if first <= range_limit:
        print(first, end=" ")

    if second <= range_limit:
        print(second, end=" ")

    while True:
        next_fib = first + second
        if next_fib <= range_limit:
            print(next_fib, end=" ")
            first = second
            second = next_fib
        else:
            break 

    print()
