a=5
b=10


a = b+a
b =   a - b
a = a - b 
typeOf = float(a)
# print()
# print(type(typeOf))
# for  i in range(1,10,):
#     for j in range(1,10):
#      print()


foruths = ["mango","apple","banana",7,56,456,] 
length = len(foruths)
foruths.append("peyara") 
foruths.remove("apple")
   
nmbrlisr =[]
for fruot in foruths:
 print(fruot)
 if type(fruot) == int:
   nmbrlisr.append(fruot)
print(nmbrlisr)  

student = {
  "name":"Hmaza",
  "age":22,
  "dep": "C.s.t"
}
# for man,mans in student.items():
#   print(man,mans)
# print(student["age"])