# 6. Write a Python program to read a file line by line and store it into a list.
'''
 file = open('output1.txt', 'r')
 print(file.readlines())
 file.close()
 
'''
##################################################################################################################################################

# 7. Write a Python program to read a file line by line store it into a variable.
'''
 file = open('file_name.txt', 'r')
 str=""
 for i in range(0,100):
    str=str + f.read(i)

print(str)
 
'''
##################################################################################################################################################

# 8. Write a python program to find the longest words.
"""
def longest_word(file_name):

  with open(file_name.txt, 'r') as infile:
      words = infile.read().split()
      
  max_len = len(max(words, key = len))
  return [word for word in words if len(word) == max_len]

print(longest_word('file_name.txt'))     
"""
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
    open("file_name.txt")

    return Counter(file_name.read().split())

print("Number of words in the file: ", word_count("file_name.txt")) 

"""
##################################################################################################################################################






 