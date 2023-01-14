a= int(input("Enter the range:"))
A=[]
for i in range(a):
        b=eval(input("Enter the element:"))
        A.append(b)
c=sorted(A)
print(c)
m=int(input("M:"))
n=int(input("N:"))
s=c[-m]+c[n-1]
d=c[-m]-c[n-1]
print("Mth maximum:",c[-m])
print("Nth maximum:",c[n-1])
print("Sum:",0)
print("DIFFERENCE;",d)
