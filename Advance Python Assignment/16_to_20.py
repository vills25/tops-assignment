# 16. Can one block of except statements handle multiple exception ?
'''
Yes, one block of except statments handle multiple exception.

'''
##################################################################################################################################################

# 17. When is the finally block executed? 
'''
Finally block will always executes. even there are exceptions.
Finally block will print data anyway.
'''
##################################################################################################################################################

# 18. What happens when "1"== 1 is executed?

print("1" == 1)
''' Output --->> False '''

##################################################################################################################################################

# 19. How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

"""
print("start")
try:
    a = int(input("Enter something: "))
    print(10/a)
except ZeroDivisionError:
    print("You can not divide by zero")
finally:
    print("I will print any-way")
print("end")
"""
##################################################################################################################################################

# 20. Write python program that user to enter only odd numbers, else will raise an exception. 

"""
num = (int(input("Enter a odd number only: ")))
if num % 2 != 0:
    raise ValueError(input("you entered even number, enter odd number only: "))
print("Entered number is Odd.")
"""
##################################################################################################################################################

      




