Dymond_Size = int(input("Enter your dimond size : "))
for Main in range(Dymond_Size):
    for sps in range(Dymond_Size - Main):
        print(" ",end=" ")
    for str in range(Main):
        print("*",end=" ")
    for str in range(Main):
        print("*",end=" ")
    print()        
for Main in range(Dymond_Size):
    for sps in range(Main):
        print(" ",end=" ")
    for str in range(Dymond_Size - Main):
        print("*",end=" ")
    for str in range(Dymond_Size - Main):
        print("*",end=" ")
    print()   