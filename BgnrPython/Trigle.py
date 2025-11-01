import math\

a = int(input("Enter your a number:-"))
b = int(input("Enter your b number:-"))
c = int(input("Enter your c number:-"))
s = (a*b*c)/2
area = math.sqrts*(s*(s-a)*(s-b)*(s-c))
print("Your Tringle Area:-",area)

# Somodi bahu trivuj
a = int(input("Enter your a number:-"))
b = int(input("Enter your b number:-"))
h = int(input("Enter your h number:-"))
Area = 0.5*(a+b)*h
print (Area)

# celsius to fahrenheit
Celsius = float(input("Enter yyour temperature"))
Fahrenheit = (Celsius*9/5)+32
print(Fahrenheit)