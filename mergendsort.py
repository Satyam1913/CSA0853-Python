l1=[]
l2=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    a=int(input("Enter the elment:"))
    l1.append(a)
n2=int(input("Enter the number of elements:"))
for i in range (1,n2+1):
    b=int(input("Enter the element:"))
    l2.append(b)
l3=l1+l2
l3.sort()
print("Sorted list is:",13)
