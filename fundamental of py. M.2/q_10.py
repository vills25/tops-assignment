#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

a = int(input("enter a "))

b = int(input("enter b "))

def result(a, b):

   if(a == b or abs(a-b) == 5 or abs(a+b) == 5):

       return True

   else:

       return False

print(result(a, b))