class complex :
    def __init__(self , real , image ):
        self.real = real
        self.image = image
    
    #operator overriding 
    def __add__ (self  , other ):
        new_real = self.real + other.real 
        new_imgae = self.image + other.image
        return complex(new_real , new_imgae)
        
    def display(self):
        print(f"Result is {self.real} , {self.image}")
        
c1 = complex(2,3) 
c2 = complex(2,4) 
c3 = c1+c2
c3.display()