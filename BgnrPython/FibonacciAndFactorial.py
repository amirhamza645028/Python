# FibonacciAndFactorial.py
n= int(input("Enter termers:- "))
a,b =0,1
for _ in range(n):
    print(a,end="")
    a,b = b, a+b

#            ****************************************************

n = int(input("enter number "))
fact = 1 
for i in range(1,n+1):
    fact += i 
    print("Factorial:",fact)