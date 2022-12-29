list=[1,2,3,4,5,6,7,8,9]
search=int(input("Enter the search number:"))
for i in range (0,len(list)):
    if search==list[i]:
        print(i)
