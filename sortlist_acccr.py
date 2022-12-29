a=[]
n=int(input("Enter the number of element:"))
for i in range(1,n+1):
    b=input("Enter the element:")
    a.append(b)
a.sort(key=len)
print("list of sorted elements according to their length",a)
