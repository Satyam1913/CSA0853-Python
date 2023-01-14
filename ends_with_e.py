a=input("Enter the String:")
print("Words ending with 'e':")
word=a.endswith("")
for word in a:
    if word[0]=="e":
        print(word)
