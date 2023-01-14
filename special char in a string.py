string=input("Enter the string :")
alphabets=digits=special=0
for i in range(len(string)):
    if(string[i].isalpha()):
        continue
    elif(string[i].isdigit()):
        continue
    else:
        special=special+1
print("Total Number of special character in the string:",special)
