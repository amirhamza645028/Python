Mark = int(input("Enter your mark:-"))
gread = [
   { "min":80, "Gread" :"A+"},
   { "min":70, "Gread" :"b+"},
   { "min":60, "Gread" :"c+"},
   { "min":50, "Gread" :"d+"},
    
]
result = "unknown"
for Markdic in gread:
    if Mark >=  Markdic["min"]:
        result = Markdic["Gread"]
        break
print("Your result :-",result)