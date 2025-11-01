

score = 0
q1 = input( "what is capital city of Bangladesh?")
if q1 == "dhaka":
    score += 1
elif q1 != "dhaka":
    score -= 0.5
print("This is your score", score)
q2 = input("what is the anwers of sum => 5+5 = ")
if q2 == "10" :
    score += 1
elif q2 != "10":
    score -= 0.5
print("Your score:-",score)
if score == 2 :
    score += 2
# elif q1 == "dhaka" and q2 != "10" or q1 !="dhaka" and q2 != "10":
#     score +=0
# elif q1 != q2 : 
    # score -= 1
print("Your Bonuch score", score)
# val = q1+ q2
# print("total score:-",val)


















