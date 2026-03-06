f = open("./number.txt","r")
content = f.read()
word = content.split()
sumofnumber=0

for w in word:
    sumofnumber = sumofnumber + int(w)
f.close()

f = open("./fileout.txt","w")
f.write("The sum of number is : "+ str(sumofnumber))
f.close()
