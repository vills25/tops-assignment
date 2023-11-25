#Write a Python program to get the Fibonacci series of given range. 

n = int(input ("Enter the number: "))     

a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ")             
    c = a+b                     
    a = b                
    b = c  
