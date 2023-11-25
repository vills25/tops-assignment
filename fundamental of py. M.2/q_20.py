#Write a Python function that takes a list of words and returns the length of the longest one. 

str = input("Enter a String: ")

word_list = str.split()

longest_word = max(word_list, key = len)

print("Longest word: ",longest_word)
