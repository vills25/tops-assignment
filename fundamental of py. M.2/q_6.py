# Write python program that swap two number with temp variable and without temp variable.  

# swapping of two variables with using temp variables.

x = 10
y = 50

temp = x
x = y
y = temp

print("Value of x:", x)
print("Value of y:", y)


# swapping of two variables without using temp variables.


x = 10
y = 50

x, y = y, x

print("Value of x:", x)
print("Value of y:", y)
