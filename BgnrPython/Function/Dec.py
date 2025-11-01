def decorator (func):
    def warapper():
        print("My fast decorator")
        func()
        print("My Last decorator")
    return warapper

def sum():
    print("This is second line") 
my_sum = decorator(sum)
my_sum()