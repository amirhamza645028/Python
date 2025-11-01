
q1 = input( "what is capital city of Bangladesh?")
if q1 == "dhaka":
    incmtn1= 1
elif q1 != "dhaka":
    incmtn1= -0.5
print("This is your score", incmtn1)
q2 = input("what is the anwers of sum => 5+5 = ")
if q2 == "10" :
     incmtn2= 1+1
elif q2 != 10:
   incmtn2= -0.5-0.5
print("Your score:-",incmtn2)
if q1=="dhaka" and q2== "10":
    BonuchIncrmnt = incmtn2 + 2
elif q1 == "dhaka" and q2 != "10" or q1 !="dhaka" and q2 != "10":
     BonuchIncrmnt = incmtn2 +0

print("Your Bonuch score", BonuchIncrmnt)