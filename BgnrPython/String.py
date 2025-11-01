#            speace diye bodle daw


# String e change korte text.replace

Text = "amir hamza"
changeText = Text.replace("amir", "Md")
print(changeText)


# tuple e change korte tuple(s.replace("amirhamza","Md")for s in Text)
newTextuple = ["amirhamza","hamz" ]
newTextuple = tuple(s.replace("amir","_hamza_",)for s in newTextuple)
print(newTextuple)

# use count 
thisCount = " i am politicyan and i am programer "
# enw_coundt= thisCount.count("i am politicyan and i am programer")
enw_coundt= thisCount.find("and")
print(enw_coundt)

# join 
join = ["i" ,"love" ,"you "]
JoinSentece = " ".join(join)
print("this sentence is join :",JoinSentece)

# split
SplitText = "I am a programmer and i am a polytecian"
NewSplitText = SplitText.split(" ",3)
# for i in NewSplitText:
#     print("THis is part by part ",i)

print(NewSplitText)
# revers
ReversNumber = "Reverce"
ChangeReverge = ReversNumber[::-3]
print(ChangeReverge)


# Borohater word alada kora
# sentece="AmirHamza"
# upercase = [char for char in input.str if sentece.isupper()]
# print(upercase)

# sorted
numrberr= [4,56,67,17,4,6,7,8,5,6,6,1,7,56,7,5,6,]
# squre
numrberrSqure = map(lambda x: x**2,numrberr)
print(numrberrSqure)
print(list(numrberrSqure)) 
# even or odd
evenNumber = filter(lambda x: x%2==0,numrberr)
print(evenNumber)
print(list(evenNumber))
for i in sorted(numrberr):
    print(i)

# 