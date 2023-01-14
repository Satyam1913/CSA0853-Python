n=input("Enter the string:")
vowels=0
consonants=0
max(vowels,consonants)
for i in n:
    if(i=='a' or i=='e' or i== '1' or i=='o' or i=='u' or i=='A' or i =='E' or i=='I' or i=='u'):
       vowels=vowels+1
    else:
        consonants=consonants+1
print("Total Number of Vowels in this String =", vowels)
print("Total number of consonants in thisstring=",consonants)
print("Maximum is ",max(vowels,consonants))
if max(vowels,consonants)==consonants:
      print("maximum is consonants")

else:
      print("maximum is vowels")
      
