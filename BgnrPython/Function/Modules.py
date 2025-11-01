# ************************************************************************
# Ek Modules theke ar ek Modules e call kora jay . Call korte hole Import korte hoy jake ba jei file ke call kora hobe take import korte hoy  

# Je file ba modules theke call kora hoy take bola hoy Main Modules jake call kora hoy ta ke bola hoy additional(eta Print(__name__) thakle outpu addidetional file jei namm sei file name tai print hobe) modules
# ************************************************************************


def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b

def somePrint():
    print("This is Addtional Modules")
if __name__ == "__main__":
    somePrint()
else:
    print("This not call ")

import sys 
sys.getrecursionlimit()

print(sys.getrecursionlimit())
i = 0
def InfitiveReCoursor():
    global i
    i += 1
    print("This is InfitiveReCoursor",i)
    # InfitiveReCoursor()
InfitiveReCoursor()
# ---------------------------------------------------------------------
#  python e reCoursor jeta nijei nije ke call kore and inifitive result dey(1000 til) import sys diye reCoursor  er a to z memoriallocation kora jay , ekhane ekta condition dile sei porjonto exicute hobe
