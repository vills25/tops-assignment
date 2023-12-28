# Q.31 How will you create a dictionary using tuples in python? 

# dict = {'Name': ('Vishal Sohaliya', '9033412563'), 'name': ('Vishal Patel', 'vishalsohaliya@gmail.com')}
# print(dict)

##################################################################################################################################################

# Q.32 Write a Python script to sort (ascending and descending) a dictionary by value.

# ascending
# abc = {'vishal', 'sureshbhai', 'aman', 'chaman', 'gagan', 'baman'}

# a = sorted(abc)

# print(a)

# # Decending 
# xyz = {'vishal', 'sureshbhai', 'aman', 'chaman', 'gagan', 'baman'}

# d = sorted(xyz)
# print(xyz)

#################################################################################################################################################

# Q.33 Write a Python script to concatenate following dictionaries to create a new one. 

# Details = {

#             'Vishal':{
#                 'mobile':['9033478555'],
#                 'email':'vishal@123456',
#                 'batch':'Python backend'
#                 }
#          }       

# Details2 = {
            
#             'Brijesh':{
#                 'mobile':['1234567890','9033478900'],
#                 'email':'brijesh@gmail.com',
#                 'batch':'python fullstack'
    
#            }
# }

# Details.update(Details2)
# print(Details)

###########################################################################################################################################

# Q.34  Write a Python script to check if a given key already exists in a dictionary. 

# dict = {'apple': 5, 'banana': 10, 'orange': 7}

# given_key = 'banana'

# key_exists = given_key in locals() or given_key in globals() or given_key in vars()

# if key_exists:
#     print(f"The key '{given_key}' exists in the dictionary.")
# else:
#     print(f"The key '{given_key}' does not exist in the dictionary.")

###########################################################################################################################################

# Q.35 How Do You Traverse Through A Dictionary Object In Python?

# my_dict = {
#     "name": "John Doe",
#     "age": 30,
#     "occupation": "Software Engineer"
# }

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)    

############################################################################################################################################

# Q.36 How Do You Check The Presence Of A Key In A Dictionary?

'''
Here are some other ways to check if a key exists in a dictionary in Python: 
--> keys() function: Returns a list of keys in the dictionary
--> get() method: Returns a list of available keys in the dictionary
--> setdefault() method: Checks if a key exists in a dictionary

You can also use the del keyword to remove a key-value pair from a dictionary. 
The pop() method can be used to remove a key-value pair and also get the value of the key-value pair. 
In C#, you can use ContainsKey() to check if a key exists in a dictionary. This returns true if the key is present, and false if it is not. 
'''    
############################################################################################################################################

# Q.37 Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

# dict = {}

# for num in range(1, 16):
#     dict[num] = num ** 2

# print("Dictionary with squares of keys:")
# print(dict)

########################################################################################################################################

# Q.38 Write a Python script to merge two Python dictionaries.

# Details = {

#             'Vishal':{
#                 'mobile':['9033478555'],
#                 'email':'vishal@123456',
#                 'batch':'Python backend'
#                 }
#          }       

# Details2 = {
            
#             'Brijesh':{
#                 'mobile':['1234567890','9033478900'],
#                 'email':'brijesh@gmail.com',
#                 'batch':'python fullstack'
    
#            }
# }

# Details.update(Details2)
# print(Details)

###############################################################################################################################################

# Q.39 Write a Python program to map two lists into a dictionary.

# keys = ['email', 'id', 'psky']

# values = ['vish@123', '#12345', '#f1985']

# dictionary = dict(zip(keys, values))

# print(dictionary)

#######################################################################################################################################

# Q.40 write a Python program to combine two dictionary adding values for common keys. 

# from collections import Counter

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}

# counter_d1 = Counter(d1)
# counter_d2 = Counter(d2)

# combined_counter = counter_d1 + counter_d2

# print(combined_counter)
