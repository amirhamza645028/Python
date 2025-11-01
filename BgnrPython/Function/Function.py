def sum (some):
    print(sum)
    scqure= some*2
    return scqure

sumResult = sum(5)
print("this is your sum ",sumResult)

def CalculatorsTupel (a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    divid = a/b
    return sum,sub,mul,divid
TOtal = CalculatorsTupel(10,5)
print("This your total man:",TOtal)    

# *args → অসীম argument ,,যখন জানো না কয়টা parameter আসবে, তখন ব্যবহার করবে।
def ManyArguments (*agrum):
     
     return sum(agrum)
sumition = ManyArguments(3,45,67,85,4,5,6,7)
print(sumition)

# 🔹 4. **kwargs → অসীম keyword argument
# এখানে নামসহ argument পাঠানো হয়
# ফাংশনের ভেতরে return একবার execute হলেই loop থেমে যায়।
def Multiplkeys (**keys):
    TOtall =""
    for key,value in keys.items():
         TOtall+= f"{key} = {value}\n"
    return TOtall
# Intiduce = {name="Hamza", age=22, country="Bangladesh"}
Multiplkey = Multiplkeys(name="Hamza", age=22, country="Bangladesh" )
print (Multiplkey)

# double function

def Outer(funIn,*value):
    return funIn(value)
def Inner (x):
    return x*2
Fastfunction = Outer(Inner,10,567,56)
print(Fastfunction)
