# Q.1 What is List? How will you reverse a list? 

"""
List is ordered. 
List allowes duplicate values.
List is mutable means its changable.

In Python, a list is a built-in data structure that allows you to store and manipulate a collection of items. 
Lists are defined by enclosing a comma-separated sequence of items within square brackets [ ]. 

syntax : 
list_name = []
list_name = list() --Function

"""
# To revers a list
# Here we will use 'reverse' function.
# products.reverse()
# print(products) 

# list1 = [2, 33, 222, 14, 25]

# list1.reverse()

# print(list1)
    

###################################################################################################################################################

# Q.2 How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

# One way is to use the pop() method. This method removes the last element of a list by default,
# or you can specify the index of the element you want to remove.
  
  #EXAMPLE 
  
# list1 = [2, 33, 222, 14, 25]

# list1.pop(2) # for removing the object on second index. output [2, 33, 14, 25]

# print(list1)
    
###################################################################################################################################################

# Q.3 Differentiate between append () and extend () methods?

'''
---Append method

It adds an element at the end of the list. The argument passed in the append function is added as a single element at end of the list and 
the length of the list is increased by 1.
The element can be a string, integer, tuple, or another list.

Syntax:
list_name.append(element)

Example:
        list_1 = [1, 2, 3]

        list_1.append(4)

        print(list_1)

---Extend method
This method appends each element of the iterable (tuple, string, or list) to the end of the list and increases the length of the list by 
the number of elements of the iterable passed as an argument.

Syntax:
list_name.extend(iterable)

Example:
        list_2 = [1, 2, 3]

        list_2.extend([4, 5, 6])

        print(list_2)
 

''' 

##################################################################################################################################################

# Q.4 Write a Python function to get the largest number, smallest number and sum of all from a list. 

# number=[30,76,50,94,16,25,100,67]

# number.sort()

# print("largest elements is: ",number[7])

# print("Smallest elements is: ",number[0])

# print(sum(number))  

################################################################################################################################################## 

# Q.5 How will you compare two lists? 

'''
Equality (==) and Inequality (!=):

The equality operator (==) checks if both lists have the same elements in the same order.
If all elements in both lists are equal at corresponding indices, and both lists have the same length, they are considered equal.

The inequality operator (!=) checks if the lists are not equal.

'''   

##################################################################################################################################################

# Q.6 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same 
#     from a given list of strings.  

# list=["madem","3643","apple","3753"]
# ch = 0
# for list in list:
# 	if len(list) > 1 and list[0] == list[-1]:
# 	  ch += 1
# print(ch)

##################################################################################################################################################

# Q.7 Write a Python program to remove duplicates from a list.  

# duplicates = [2, 4, 10, 20, 5, 2, 20, 4]
# print(set(duplicates))

##################################################################################################################################################

# Q.8 Write a Python program to check a list is empty or not.

# list = [1,"Vishal", 25,]

# if len(list) == 0:
#   print("The list is empty.")
# else:
#   print("The list is not empty.")

##################################################################################################################################################

# Q.9 Write a Python function that takes two lists and returns true if they have at least one common member.

# list1=[1,2,3,4,5]
# list2=[5,6,7,8,9]
# result = False
# for x in list1:
#  for y in list2:
# 	 if x == y:
# 		 result = True
# print(result)
# if result:
#     print("Lists have at least one common member")
# else:
#     print("Lists do not have any common member")

##################################################################################################################################################

# Q.10 Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

# l = list()
# for i in range(11,25):
# 	l.append(i**2)
# print(l[:5])
# print(l[-5:])

##################################################################################################################################################
