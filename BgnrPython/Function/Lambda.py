num =[4,3,5,7,8,65,5,34,3,5,67]

scqure = list(map(lambda x: x*x,num))
# print(scqure)
# map and filter ekta funtion ney , pore ekta sequence ney
EvnOdd = list(filter(lambda x: x%2==0,num))
# print("this even:",EvnOdd)

Add = lambda x,y: x+y
# print(Add(3,4))

# list lambda
li =[4,5,7,4,6,7,85,778,4,6]
Even = (lambda *x : x%2==0,li)
print(Even(li))
