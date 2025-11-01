NameSIze = int(input("ENTER YOUR NAME SIZE : "))
for NRow in range(NameSIze):
    for ncolm in range(NameSIze+1):
        if ncolm == NameSIze:
           print("*") 
    for ncolm in range(3,NRow):
           print(" ")
    for ncolm in range(1,NameSIze+1):
        if ncolm == NameSIze:
           print("*") 
    for ncolm in range(NameSIze-NRow):
           print(" ")  
    for ncolm in range(1,NameSIze+1):
        if ncolm == NameSIze:
           print("*")            
    print()


NameSize = int(input("ENTER YOUR NAME SIZE : "))

for row in range(NameSize):
    for col in range( ):
        if col == 0 or col == NameSize-1 or col == row:
            print("*", end="")   # পাশাপাশি প্রিন্ট করার জন্য end=""
        else:
            print(" ", end="")   # ফাঁকা জায়গা
    print()   # প্রতিবার row শেষে নতুন লাইন
