#Factorial_Recursion
def recursive_factorial(n):
  if n==1:
     return n
  else:
     return n*recursive_factorial(n-1)    
n=int(input("Enter the factorial number: "))
print("The factorial of", n, recursive_factorial(n))
