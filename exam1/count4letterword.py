f = open("./woordd.txt","r")
count=0
content = f.read()
word = content.split()
for w in word:
    if len(w) == 4:
        print(w)
        count+=1
print("Count of 4 letter word in the file : ",count)
f.close()