# Q.11 Write a Python function that takes a list and returns a new list with unique elements of the first list. 

# list1 = [10, 20, 10, 30, 40, 40]

# unique_list_1 = list(dict.fromkeys(list1))

# print(unique_list_1)

#################################################################################################################################################

# Q.12   Write a Python program to convert a list of characters into a string.  

# s = ['V', 'I', 'S', 'H', 'A', 'L']
# str1 = ''.join(s)
# print(str1)

#################################################################################################################################################

# Q.13 Write a Python program to select an item randomly from a list.

# import random 

# my_list = [1, 'a', 32, 'c', 'd', 31]

# print(random.choice(my_list))


#################################################################################################################################################

# Q.14 Write a Python program to find the second smallest number in a list.

# list1 = [50, 40, 0, 30, 10,]

# sortlist = sorted(list1)
 
# second_lowest = sortlist[1]
 
# print(second_lowest)

#################################################################################################################################################

# Q.15 Write a Python program to get unique values from a list 
# items = [11,11,25,10,22,30,22,25,30,30,10,11]

# print(set(items))

#################################################################################################################################################

# Q.16 Write a Python program to check whether a list contains a sub list 

# list = [[1,5,7,], [2, 3, 4], [3, 6, 9], [4, 8, 12]] 
# check_list = [2,3,4]

# if check_list in list: 
# 	print("list contains a sub list") 
# else: 
# 	print("list is not contains a sub list") 
 
#################################################################################################################################################

# Q.17 Write a Python program to split a list into different variables.  

list1 = ['Vishal', 'Sureshbhai', 'Sohalia']

var1, var2, var3 = list1

print(var1)
print(var2)
print(var3)

#################################################################################################################################################

# Q.18 What is tuple? Difference between list and tuple. 

'''
# TUPLE
#tuple is a collection of elements of similar or different datatype
# tuple is immutable------no changes are allowed
# tuple is ordered--------every elements in list has its own index number
# tuple is defined in () brackets
# tuple allows duplicates values because they all have different index numbers
'''

'''
DIFFRENCE BETWEEN LIST AND TUPLE---

1. Mutability:
   - List: Lists are mutable, which means you can change, add, or remove elements after creating the list. You can use methods like append(), 
     extend(), insert(), and remove() to modify a list.
   - Tuple: Tuples are immutable, meaning once you create a tuple, you cannot change its content. You cannot add or remove elements from a tuple.
     This immutability can be useful in cases where you want to ensure that the data remains constant.

2. Syntax:
   - List: Lists are created using square brackets, for example, my_list = [1, 2, 3].
   - Tuple: Tuples are created using parentheses, for example, my_tuple = (1, 2, 3). You can also create a tuple without parentheses, e.g.,
     my_tuple = 1, 2, 3.

3. Performance:
   - Lists, being mutable, can be less memory-efficient and slower in certain operations compared to tuples.
   - Tuples, being immutable, are generally more memory-efficient and faster for simple operations, making them a better choice when you need to 
     store data that should not change.

4. Use Cases:
   - Lists are often used for collections of items where you may need to add, remove, or modify elements during the program's execution.
   - Tuples are typically used when you want to ensure that the data remains constant and should not be changed, such as representing coordinates,
     dates, or configurations.

5. Iteration:
   - Both lists and tuples can be iterated using loops like `for` or by using list comprehensions. Iterating through a tuple can be slightly faster
     due to its immutability.

'''

##################################################################################################################################################

# Q.19. Write a Python program to create a tuple with different data types.

# A=(35,45.87,True,"hello",[24,75,34],(32,66),{1,2},{1:"hello",2:"python"})
# print(type(A))

##################################################################################################################################################

# Q.20 Write a Python program to create a tuple with numbers.

# x= (12,23,45)
# print(x)

##################################################################################################################################################



  


    