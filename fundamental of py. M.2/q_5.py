# What is the purpose continue statement in python?  

'''
The continue statement in Python is used to skip the remaining code inside a loop for the current iteration only.
A continue statement ends the current iteration of a loop. Program control is passed from the continue statement to the end of the loop body.
A continue statement can only appear within the body of an iterative statement, such as do , for , or while .

'''
#Example

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



for i in number_list:

  if i % 2 == 0:

    continue

  print(i)
