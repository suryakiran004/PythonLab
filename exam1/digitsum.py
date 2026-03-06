n = int(input("Enter a number : "))
sumofdigit = 0
rev =0 
temp =n 

while n>0:
    d = n%10
    sumofdigit += d
    rev = rev*10 + d
    n = n//10
print("Original number : ",temp)
print("Reversed number :",rev)
print("Sum of digit :",sumofdigit)
