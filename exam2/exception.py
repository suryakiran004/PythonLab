try:
    x = int (input ("Enter a number as value : "))
    result = 50 / x
    

except ValueError:
    print("Please enter a valid input !")
    
except ZeroDivisionError :
    print("Zero cannot be divided !")

else :
    print(result)
    
finally :
    print("program executed successfully !")