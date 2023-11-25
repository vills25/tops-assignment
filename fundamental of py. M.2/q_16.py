#  Write a Python program to count the occurrences of each word in a given sentence.  

str = input("Enter Sentence: ")
count = dict()

txt = str.split(" ")
for j in txt:
	if j in count:
		count[j] += 1
	else:
		count[j] = 1
  
print(count)