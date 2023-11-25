# Write a Python program to count the number of characters (character frequency) in a string.  

string = input("Enter String: ")
lis=list(string)

frequency =[lis.count(elements) for elements in lis]
a = dict(zip(lis,frequency))

print(a) 
