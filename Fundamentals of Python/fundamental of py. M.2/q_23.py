# Write a Python function to insert a string in the middle of a string.

original_string = input("Enter a string: ")
string_to_insert = input("Enter a string to insert: ")

middle_index = len(original_string) // 2
result = original_string[:middle_index] + string_to_insert + " " + original_string[middle_index:]

print(result)
