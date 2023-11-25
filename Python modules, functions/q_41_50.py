

# Q.41 Write a Python program to print all unique values in a dictionary. 

# dict = {
#     'vishal': '25',
#     'sureshbhai': '30',
#     'vishal': '25',
#     'sureshbhai': '30',
#     'aman': '45',
#     'aman': '45'
# }

# print("Original Dictionary: ", dict)

# unique_values = set(dict.values())

# print("Unique Values: ", unique_values)

############################################################################################################################################

# Q.42  Why Do You Use the Zip () Method in Python? 

'''
The zip() function in Python is used to combine multiple iterables (lists, tuples, etc.) element-wise into an iterator of tuples. 
It's particularly helpful when you want to iterate through multiple sequences simultaneously.

Iterating Through Multiple Iterables Simultaneously-->> If you have several lists (or any iterables) and you want to work with their elements together, 
zip() allows you to iterate over them in parallel.

Creating Dictionaries-->> Using zip() with two lists, you can easily create a dictionary where one list contains keys and the other contains values.

Unzipping-->> You can also use zip() in combination with the * operator to unzip a list of tuples into separate lists.

zip() is a versatile function that aids in handling multiple iterables efficiently, enabling operations like iteration, creation, and transformation 
of data between different structures.

'''
############################################################################################################################################

# Q.43 Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
       # Sample data: {'1': ['a','b'], '2': ['c','d']}

# from itertools import product

# data = {'1': ['a', 'b'], '2': ['c', 'd']}

# combinations = list(product(*(data[key] for key in data)))
# for combination in combinations:
#     print(''.join(combination))

############################################################################################################################################

# Q.44 Write a Python program to find the highest 3 values in a dictionary.

# sample_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

# highest_values = sorted(sample_dict.values(), reverse=True)[:3]

# print("The highest 3 values in the dictionary are:", highest_values)

############################################################################################################################################

# Q.45 Write a Python program to combine values in python list of dictionaries.

# data = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750}
# ]

# combined_data = {}
# for entry in data:
#     item = entry['item']
#     amount = entry['amount']
#     if item in combined_data:
#         combined_data[item] += amount
#     else:
#         combined_data[item] = amount

# print(combined_data)

###########################################################################################################################################

# Q.46 Write a Python program to create a dictionary from a string.

# input_string = "hello"
# dict = {}

# for char in input_string:
#     if char in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1

# print(dict)

###########################################################################################################################################

# Q.47 Write a Python function to calculate the factorial of a number.

# import math

# print(math.factorial(int(input("Enter number: "))))

###########################################################################################################################################

# Q.48 Write a Python function to check whether a number is in a given range.

# def count(list1, s, e):
# 	return len(list(filter(lambda x: s <= x <= e, list1)))

# list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
# s = 20
# e = 40
# print(count(list1, s, e))

#output Will be 5 

###########################################################################################################################################

# Q.49 Write a Python function to check whether a number is perfect or not. 

# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if (sum1 == n):
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")

###########################################################################################################################################

# Q.50  Write a Python function that checks whether a passed string is palindrome or not.

# def palindrom(string):
#        reversestring=''.join(reversed(string))
#        if string == reversestring:
#               return 'The string is palindrom.'
#        return 'Thre string is not palindrom.'

# print(palindrom(input('Enter a string: ')))

###########################################################################################################################################