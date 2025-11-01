SesionMonth = int(input("Enter your month(1-12):-"))
if SesionMonth in [12,2,1]:
    print("winter")
elif SesionMonth in [3,4,5]:
    print("spring")
elif SesionMonth in [6,7,8]:
    print("Summer")
else:
    print("Autumn")
