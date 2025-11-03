class student:
    def __init__(self,data):
         for key,vlaue in data.items():
              setattr(self , key,vlaue)
    def __str__(self):
         return f"Your keys : {self.key} , {self.vlaue}:"
    # def __str__(self):
    #      return str(self.__dict__)
data = {
     "amir":'hamza',
     "amfir":'hadfmza',
     "amdfir":'hadzmza',
     "amidfr":'hamdxfza',
}  
studentObj = student(data)   
print(studentObj)         