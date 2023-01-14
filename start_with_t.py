a=input("Enter the String:")
print("Words starting with 'T'")
words=a.startswith("T")
for word in words :
    if word[0]=="t":
        print(word)
