# Write a Python program to count the number of characters (character frequency) in a string.  

# naive method

test_str = "Vishal Sohaliya"

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print("Count of all characters in Vishal Sohaliya is :\n "
	+ str(all_freq))
