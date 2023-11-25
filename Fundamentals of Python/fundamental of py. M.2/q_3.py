#Write a Python program to get the Fibonacci series of given range. 

n = int(input ("Enter the number: "))     

a = 0    
b = 1    
c = 0

while (c<=n):
    print(c) 
  
    a = b
    b = c
    c = a+b