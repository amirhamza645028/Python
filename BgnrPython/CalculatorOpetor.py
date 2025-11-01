a= float(input(" Enter your Number :-"))
b= float(input("Enter your Number;-"))

op = input(" Enter your Operator (=,-,*,/,%,**):")
if op == "+":
    print("Your summition :-", a +b)
elif op == "-":
    print("YOur subtection:-",a-b)
elif op == "*":
    print("YOur subtection:-",a*b)
elif op == "/":
    print("YOur Divition:-",a/b)
elif op == "%":
    print("YOur Musolusch:-",a%b)
elif op == "**":
    print("YOur Power:-",a**b)
elif a or b != float or int:
    print("Invalid Number")
else:
    print("No Calculation Error _402")
