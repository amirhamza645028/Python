# sentence = [ "i am amirhamza i come form faridpur sadarpur to be more exact Right now i am student at european it solution"]
# Newwords = []
# Words = sentence.split()
# for word in Words:
#     if len(word)>5: 
#         Newwords.append(word)
# for word in sentence:
#     words = word.split()
#     if len(words) > 5:
#         Newwords.append(words)
# print("THIS IS NEW WORDS : ", Newwords)

# checkList = ["nhgd#", "Hamza123", "12345", "helloWorld"]

# for alfas in checkList:
#     if len(alfas)==0:
#       print("empty")
#       continue

#     is_alfa = True
#     for alfa in alfas:
            
#       if "a"<= alfa <= "z" or "A"<= alfa <= "Z" or "0"<= alfa <= "9" :
#        pass
#       else:
#         is_alfa = False
#     if is_alfa:
#       print(f"{alfa}--> This is AlfaNumeric")
#     else:
#       print(f"{alfa}--> This is not AlfaNumeric")    
# 
# def isalphanum (D):
   
#     if len(D)==0:
#         return False
#     for ch in D:
            
#         if "a"<= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9":
#            pass
#         else:
#             return False
#     return True    

# checkList = ["nhgd#", "Hamza123", "12345", "helloWorld"]
# for C in checkList:
#     print(f"{C!r:12} -> {isalphanum(C)}")

# find digit , lowerCase, UperCase
digit = 0
Lower = 0
UperCase =0 

allNumber = ["aklsudyf4378fGDUeiw48fvnF"]
# for i in allNumber:
#   print(i)
#   Case = ord(i)
#   if 65 <= Case <=90:
#     UperCase =+1
#   if 97 <= Case <=122:
#     Lower =+1
#   if 48 <= Case <=57:
#     Lower =+1
# print(digit)
# print()
# ls = []
# for i in range(1,11):
#   ls.append(i**2)

# 
# for i in range(-1,5):
#   for j in range(0, (5-1)+1):
#     print("*",)
# print()    
n = 6
for i in range(n):
  for s in range(n-i):
    print(" ",end=" ",)    
  for jl in range(i):
    print("*",end=" ",)  
  for jr in range(i):
    print("*",end=" ",)
  print() 
  
n = 6
for i in range(n):
  for s in range(i):
    print(" ",end=" ",)    
  for jl in range(n-i):
    print("*",end=" ",)  
  for jr in range(n-i):
    print("*",end=" ",)
  print() 
  
