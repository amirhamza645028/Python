# ls=[]
# while True:
#     inputt = int(input("Enter your String:"))
#     if inputt == "p":
#         break
#         # pass
#         # continue
        
#     ls.append(inputt)
#     print(ls)

def my_sum (*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
# res = my_sum(*ls)  
# print(res)
# _______________________________________________________________
from time import time

def my_func (**kwargs):
    fastTime = time()
    print(kwargs     )
    name= kwargs.get("name")

    if name:
        print("find your name")
    FinishedTime = time()  
    print("Total Time :",FinishedTime-fastTime)
    return my_func
    
print((my_func(name ="amir",age=29)))    

# jekono pyhton er function paramitter hisabe pathano jay