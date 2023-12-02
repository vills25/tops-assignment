# 1. What is File function in python? What is keywords to create and write file.
'''
The file function in Python is a built-in function that takes a filename as an argument and returns a file object. 
The file object can then be used to read, write, or append data to the file.
The file function takes two arguments: the filename and the mode. The mode argument specifies how the file should be opened.

To create file:
open('file_name.txt', 'x')

To Write file:
 file = open('file_name.txt', 'w') 
 file.write("this is a python programming")
 file.close()

''' 
##################################################################################################################################################

# 2. Write a Python program to read an entire text file.
'''
To read an entire file:

 file = open('file_name.txt', 'r')
 print(file.read())
 file.close()
 
'''
##################################################################################################################################################

# 3. Write a Python program to append text to a file and display the text.
'''
 To append data into a file:
 
# file = open('output.txt', 'a')
# file.write("this is a python programming")
# file.close()
'''
##################################################################################################################################################

# 4. Write a Python program to read first n lines of a file
'''
To read first n lines of a file

 file = open('file_name.txt', 'r')
 print(file.readlines(1))
 file.close()
 
'''
##################################################################################################################################################

# 5. Write a Python program to read last n lines of a file.
'''
To read last n lines of a file

 file = open('file_name.txt', 'r')
 print(file.readlines([-1]))
 file.close()
 
'''
##################################################################################################################################################
    