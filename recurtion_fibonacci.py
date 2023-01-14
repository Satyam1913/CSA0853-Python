#fibonacci_recursion
first,second=0,1
n = int(input("please give a number for fibonacci series:"))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("fibonacci series are:")
for i in range(0,n):
    print(fibonacci(i))

