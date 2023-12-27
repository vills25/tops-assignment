# Write a Python program to count occurrences of a substring in a string. 

strings = input("Enter string: ")
substring = input("Enter Substring: ")

occurrence_count = sum(string.count(substring) for string in strings.split())

print(occurrence_count)  
 
 
 
 
 
 
 
 
 
 
 
 
