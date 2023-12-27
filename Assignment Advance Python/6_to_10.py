# 6. Write a Python program to read a file line by line and store it into a list.
'''
 file = open('output1.txt', 'r')
 print(file.readlines())
 file.close()
 
'''
##################################################################################################################################################

# 7. Write a Python program to read a file line by line store it into a variable.

# file = open('file_name.txt', 'r')
# str=""
# for i in range(0,100):
#     str=str + file.read(i)

# print(str)
 

##################################################################################################################################################

# 8. Write a python program to find the longest words.

file = open("output.txt", 'r')
words = file.read().split()
file.close()

max_len = len(max(words, key=len))
longest_words = [word for word in words if len(word) == max_len]

print(longest_words)


##################################################################################################################################################

# 9. Write a Python program to count the number of lines in a text file.
"""
file = open('file_name.txt', 'r')

lines = len(file.readlines())

print("Total number of lines: ", lines)

"""
##################################################################################################################################################

# 10. Write a Python program to count the frequency of words in a file. 

"""
from collections import Counter

def word_count(file_name):
    file = open(file_name, 'r')
    content = file.read()  
    file.close()  
    words = content.split()  
    return Counter(words)  

file_name = "output.txt"
word_counter = word_count(file_name)
print("Number of words in the file:", sum(word_counter.values()))
"""


##################################################################################################################################################






 