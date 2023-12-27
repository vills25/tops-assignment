#  Write a Python program to count the occurrences of each word in a given sentence.  

name = (input("Enter a String: "))
name = name.lower()

letter_counter = {}
empty_list = []

for ch in name:
    if ch not in empty_list:
        empty_list.append(ch)
        
for unique_ch in empty_list:
    letter_counter.setdefault(unique_ch, name.count(unique_ch))
    
print(letter_counter)            
