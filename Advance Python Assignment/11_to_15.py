# 11. Write a Python program to write a list to a file.
"""
file = open('output.txt', 'w')
file.writelines(["Vaman ", "chaman ", "baman ", "magan ","kaman ", "ghaman ", "saman ", "gagan ","raman ", "taman ", "iman ", "fagan "])
file.close()
"""
##################################################################################################################################################

# 12. Write a Python program to copy the contents of a file to another file.

"""
import shutil
shutil.copyfile('file_1','file_2')
"""
##################################################################################################################################################

# 13. Explain Exception handling? What is an Error in Python?

"""
What is exception handling?
--Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these
events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

--Exceptions occur for numerous reasons, including invalid user input, code errors, device failure, the loss of a network connection, insufficient 
memory to run an application, a memory conflict with another program, a program attempting to divide by zero or a user attempting to open files 
that are unavailable.

--When an exception occurs, specialized programming language constructs, interrupt hardware mechanisms or operating system interprocess communication
facilities handle the exception.

--Exception handling differs from error handling in that the former involves conditions an application might catch versus serious problems an 
application might want to avoid. In contrast, error handling helps maintain the normal flow of software program execution.

What is an Error in python?
--Errors are problems that occur in the program due to an illegal operation performed by the user or by the fault of a programmer, which halts the 
normal flow of the program. Errors are also termed bugs or faults. There are mainly two types of errors in python programming.

There are two types of Error in python
 --Syntax errors
 --Logical errors (Exceptions)
 
Exceptions(error) in python....

AssertionError: raised when the assert statement fails.
EOFError:       raised when the input() function meets the end-of-file condition.
AttributeError: raised when the attribute assignment or reference fails.
IndexError:     occurs when the index of a sequence is out of range
KeyboardInterrupt: raised when the user inputs interrupt keys (Ctrl + C or Delete).
RuntimeError:   occurs when an error does not fall into any category. 
NameError:      raised when a variable is not found in the local or global scope. 
ValueError:     occurs when the operation or function receives an argument with the right type but the wrong value. 
ZeroDivisionError: raised when you divide a value or variable with zero. 
SyntaxError:    raised by the parser when the Python syntax is wrong. 
IndentationError: occurs when there is a wrong indentation.
SystemError:    raised when the interpreter detects an internal error.

"""
##################################################################################################################################################

# 14. How many except statements can a try-except block have? Name Some built-in exception classes.

'''
Atleast One except statements can a try-except block.

'''
"""Here are some built-in exception classes in Python:
ArithmeticError, AttributeError, BufferError, BytesWarning, DivisionByZeroError, EOFError, FloatingPointError, IndexError, KeyError,
KeyboardInterrupt, MemoryError, NameError, NoneType, NotADirectoryError, OSError, OverflowError, ReferenceError, RuntimeWarning, StopIteration, 
StringIndexError, SystemExit, TypeError, UnboundLocalError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError, ValueError, ZeroDivisionError.
"""
##################################################################################################################################################

# 15. When will the else part of try-except-else be executed?

''' The else part is executed when no exception occurs. '''


"""
print("start")
try:
    a = int(input("Enter something: "))
except ValueError:
    print("Please enter only digit")
except NameError:
    print("Please define variable a")
except Exception as e:
    print(f"ERROR : {e}")
else:
    print(a  + 10)

print("end")

"""
##################################################################################################################################################


