s = input("Enter a string :")
d=dict()
for c in s:
    d[c] = d.get(c,0)+1
print(d)