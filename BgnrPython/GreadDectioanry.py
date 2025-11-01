Mark = int(input("Enter your mark:-"))
result = "unknown"
gread = {
    80:"A+",
    70:"B+",
    60:"B+",
    50:"C+",
    40:"D+"
}

# Ekhane dictionary ta string er moddhe likhte hobe ar javascript e simple vabe likhleo hoy

# for markSoter in sorted(gread.keys(),reverse=True):
#     if Mark >= markSoter:
#         result = gread[markSoter]
#         break
# print("Your result ",result)

for markstr in gread:
    print(markstr)    
    if Mark >= markstr:
        print(Mark)
        result = gread[markstr]
        print("this gread[]",result)
        break
print(markstr)    
print("your result :-",result)


for mark in gread:
    if Mark >= mark:
        result = gread[mark]
        