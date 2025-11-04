from datetime import date
Fixed_year = 22
class Employee:
    def __init__(self,name:str,role:str,dob:date)->None:
        self.name = name
        self.role = role
        self.dob = self.check_dob(dob) #ekhane self diye kn access korte holo check_dob ke???
        self.salry = None
        self.star = 0

    def delay(self):
        self.star += 1

    def check_dob(self,dob): #eta valid birth day diche kina ()
        current_date = date.today()
        if current_date < self.dob:
            raise ValueError(" Your date of birth is unvalid")
        User_age = self.age(Out_add_dob=dob) #ekhane aei vabe keno dilam Out_add_dob er moddhe dob kn dilam ?? age er vitore tw Out_add_dob ta ache aei tar sathei tw ami Fixed age compear korei korbo tai na ? tahole dob kn anlam ? ane ken Out_add_dob er moddhe rakhlam??
        if User_age < self.Fixed_year:
            raise ValueError("this is age error ")
        return dob
    
    def age (self,Out_add_dob =None ): #ekhane alada kore Out_add_dob pathano jaybe kintu eta ami kn pathabo ami tw user deoya dob theke user er age ber korbo ! Tahole Out_add_dob =None eta alada kore kn nilam sora sori sudhu user er deoya bod (self.dob.year) eta niye kn kaj korlam na ? baire theke pathai te hobe kn?
        current_date = date.today()
      
        if Out_add_dob:
            dob_year = Out_add_dob.year
        else:
            dob_year = self.dob.year   
        # UserAge = current_date.year - self.dob.year
        UserAge = current_date.year - dob_year
         # user er dowya date ta anbo kemne and ane korbo ki pathabo kothay
        return UserAge
    # baire theke keo jeno dob pathiye dob change kore na dite na pare eta ki vabe krobo je class er vitore chara baire theke keo kichu pathai te parbe na? eta setattr() diye korbo naki onno kono method diye?? 
    @property
    def is_Active(self)-> bool:
        if self.salry:
            return True
        return False
    

    def set_salary (self,amount)->None:
        if amount <= 0: 
            raise ValueError("this is amount error")
        if self.star > 0:
            self.salry = amount -self.star
        else:
           self.salry = amount


    def __str__(self):
        return f"your name{self.name}"
e1 = Employee(ame="Abdullah", role="admin", dob=date(1996,1,1)) 
print(e1.dob)     
e1.delay()  

# from datetime import date

# class Employee:

#     MIN_AGE = 25
#     def __init__(self, name:str, role:str, dob:date) -> None:
#         self.name = name
#         self.role = role
#         self.dob = self.check_dob(dob)
#         self.salary = None
#         self.star = 0
        
#     def delay(self):
#         self.star += 1
        
#     def check_dob(self, dob):
#         current_date = date.today()
       
#         if dob > current_date:
#             raise ValueError("DOB must be less than current date")
        
#         age = self.age(dob=dob)
#         if age < self.MIN_AGE:
#             raise ValueError(f"Employee must be minimum {self.MIN_AGE} years!")
#         return dob
    
#     def age(self , dob=None): #jodi baire theke dob pathan 
#         # Calcucate age from DOB
#         current_date = date.today()
#         # dob_year = dob.year hobe jodi dop pthano hoy ar na hole self.dob.year hobe
#         dob_year = dob.year if dob else self.dob.year
#         age = current_date.year - dob_year
#         return age  
#     @property
#     def is_active(self) -> bool:
#         if self.salary:
#             return True
#         return False
    
#     def set_salary(self, amount) -> None:
#         if amount <= 0:
#             raise ValueError("Not a valid salary")
        
#         if self.star > 0:
#             self.salary = amount - self.star
#         else:
#             self.salary = amount

#     def __str__(self):
#         return f"Employee(name={self.name})"
    

# e1 = Employee(name="Abdullah", role="admin", dob=date(1996,1,1))

# age = e1.age()

# e1.delay()
# e1.delay()
# e1.delay()

# print(e1.is_active)
# e1.set_salary(18000)
# print(e1.is_active)
# print(e1.salary)