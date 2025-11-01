# import random
class Human :
    def __init__(self,name,age,dept,institute):
        # self.id = hash(name(random.randint(1,1000)))
        self.name = name,
        self.age = age,
        self.dept = dept,
        self.institute = institute
    def __str__(self):
        return f"Student Name {self.name} Student Age is  {self.age}"
hamza = Human("Amirhamza",23,"c.s.t","fpi") 
# vlaue change
hamza.name = "amir"
# print(hamza.name)

# mobial_number aei  attribut ta ache ki na 

Set = setattr(hamza,"mobial_number", "0123456789")
print(Set)
mb = getattr(hamza , "mobial_number", "Bhai Tor Mobail Number nai")
print(mb)