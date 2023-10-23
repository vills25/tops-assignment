# Write a Python program to count occurrences of a substring in a string. 

strings = ["Red", "Green", "orange"]
char_to_count = 'e'
total_count = sum(string.count(char_to_count) for string in strings)
print(total_count) 
