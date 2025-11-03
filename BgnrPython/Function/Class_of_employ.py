   

from datetime import date

class Employee:

    MIN_AGE = 25
    def __init__(self, name:str, role:str, dob:date) -> None:
        self.name = name
        self.role = role
        self.dob = self.check_dob(dob)
        self.salary = None
        self.star = 0
        
    def delay(self):
        self.star += 1
        
    def check_dob(self, dob):
        current_date = date.today()
       
        if dob > current_date:
            raise ValueError("DOB must be less than current date")
        
        age = self.age(dob=dob)
        if age < self.MIN_AGE:
            raise ValueError(f"Employee must be minimum {self.MIN_AGE} years!")
        return dob
    
    def age(self , dob=None): #jodi baire theke dob pathan 
        # Calcucate age from DOB
        current_date = date.today()
        # dob_year = dob.year hobe jodi dop pthano hoy ar na hole self.dob.year hobe
        dob_year = dob.year if dob else self.dob.year
        age = current_date.year - dob_year
        return age  
    @property
    def is_active(self) -> bool:
        if self.salary:
            return True
        return False
    
    def set_salary(self, amount) -> None:
        if amount <= 0:
            raise ValueError("Not a valid salary")
        
        if self.star > 0:
            self.salary = amount - self.star
        else:
            self.salary = amount

    def __str__(self):
        return f"Employee(name={self.name})"
    

e1 = Employee(name="Abdullah", role="admin", dob=date(1996,1,1))

age = e1.age()

e1.delay()
e1.delay()
e1.delay()

print(e1.is_active)
e1.set_salary(18000)
print(e1.is_active)
print(e1.salary)