class Person:
    def __init__ (self , name ):
        self.name = name
    
class Employee(Person):
    def __init__(self , name , rollno):
        super().__init__ (name)
        self.rollno = rollno
        
e = Employee("Anandhu" , 32)
print(e.name , e.rollno)