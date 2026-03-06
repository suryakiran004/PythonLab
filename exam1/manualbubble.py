def bubble(n,lst):
    for i in range(n-1):
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j] , lst[i]

n=int(input("Enter the number of element : "))
lst=[]
print("Enter each element : ")
for i in range(n):
    lst.append(int(input()))
    
bubble(n,lst)
print(lst)