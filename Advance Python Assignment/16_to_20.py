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
try:
    a=int(input("Enter Numvber1: "))
    b=int(input("Enter Numvber2: "))
    print(a/b)
except ValueError as v:
    print("Integers allowed",v)
except ZeroDivisionError as z:
    print("Not allowed to divide by zero",z)
except:
    print("Unknown Error")
finally:
    print("I am part of finally and I will execute always.")
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

      




