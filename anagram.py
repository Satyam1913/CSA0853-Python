str_a=input("Enter the string_a:")
str_b=input("Enter the string_b:")
if len(str_a)!=len(str_b):
    print("It is not Anagrama")
elif sorted(str_a)==sorted(str_b):
    print("String are Anagrama")
else:
    print("It is not Anagrama")
