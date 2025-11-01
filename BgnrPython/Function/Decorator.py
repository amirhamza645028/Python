# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before function")
#         res = func(*args,**kwargs)
#         print("After Function")
#         return res
#     return wrapper

# def_mydec = decorator(sum)
# def_mydec(1,7)
# 8 and 9 line == @decorator 

# @decorator  
# def sum(a,b): return a+b 
# er mane sum = decorator(sum)


# @decorator  
# def sum(a,b):
#     """Takes two parameters and sums then"""
# # aei ta mane decorator(func) e jame decorator(sum) aei paramitter ta okk too akhon (sum) ta decorator function e giye (func) hoye jabe tahole sum er man ja ta hobe func er man  warapper er moddhe func() oii sum er man niye calculation korbe then res er vitore joma rakhbe then return kore dibe wrapper er vitoreaei warapper ta ke abar return koche decoretor er vitore ar aei decorator joma ache ? sum e  ase calcution codition sesh kore


# @decorator  
# def greet(username):
#     return f"hi {username}"

# def decorator (functin_name):
#     def innerWrrap():
#         functin_name()
#         return innerWrrap
    
# dec = decorator(my_sum)
# dec()

def test(fun):
    fun("THis is print")
test(print)