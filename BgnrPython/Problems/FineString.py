# list er moddhe number ta ache kina?
ListOfStrNbr = [4,43,6,10]
if   10 in ListOfStrNbr:
    print("yes")
else: 
    print("not funded")

# divided str and int from list
JustStr1 =[]
Justint1 =[]
LIsitWithstrAndNmbr=["bana",5,7,"apple",4,43,6,10,"ovi","naem"]
for item in LIsitWithstrAndNmbr:
    if type(item) == str  :
       JustStr1.append(item)
    else:
        # type(item)==int:
        Justint1.append(item)
    # if isinstance(item,str):
    #     JustStr1.append(item)
    # elif isinstance (item,int):
    #     Justint1.append(item)
# print("Your String list: ",JustStr1)
# print("Your Int list: ",Justint1)
# find -> unic value
unUnic = [4,45,5,4,9,54,4,4,5,434,4,5,4,3,2,24,5,6,1,7,6,88,7,5,4]
unic =[]
for U in unUnic:
    if U not in unic:
        # not in = vitore nei to na thakle append how thakle append hoi na
        unic.append(U)
print(sorted(unic))  

#  Store valid data
ValiName =[]
ValidNumber = [] 
mixed = [12, "hamza", "", None, 99, "python", False]
for UnValidNN in mixed:
    if isinstance(UnValidNN,str) and UnValidNN != "":
        ValiName.append(UnValidNN)
        # " " and None False aei gula valid na tai new list ani nai and condition diya bad diya dichi
    if isinstance(UnValidNN,int) and not isinstance(UnValidNN,bool):
        ValidNumber.append(UnValidNN)
print(ValiName)
print(ValidNumber)        

# Find user name

UserName = str(input("Enter Your Name: "))
AllName = ["Rahim","Korim ","Nur","nadiya","hamza"]
for StoreName in AllName:
    if type(UserName)== str:
        if UserName in StoreName and UserName == StoreName:
            print("Your Name is Founded") 
        elif UserName in StoreName and UserName != StoreName:
            print("Your Name is not Found")
    elif UserName not in StoreName and UserName != StoreName :
        print("THis is not valid Pleace Inter valid Text")