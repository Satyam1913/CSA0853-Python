#write a program to find number of uppercase and lowercase letters in the given string.
a=input("Enter the Word:")
u=0
l=0
for i in a:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print("The number of upper case letter{}",u)
print("The number of lower case letter{}",l)
