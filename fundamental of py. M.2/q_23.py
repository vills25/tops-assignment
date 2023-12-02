# Write a Python function to insert a string in the middle of a string.

def insert_middle(main_string, insert_string):
    middle_index = len(main_string) // 2
    result = main_string[:middle_index] + insert_string + " " + main_string[middle_index:]
    return result

original_string =(input( "Enter a string: "))
string_to_insert = (input("Enter a string which you want to insert in previous string: "))
result = insert_middle(original_string, string_to_insert)
print(result)
