r=int(input("Enter the row number:"))
c=int(input("Enter the column matrix:"))
print("Enter the elements of matrix:")
matrix=[[int(input()) for i in range (c)] for j in range(r)]
print("matrix:")
for i in range (r):
    for j in range (c):
        print(format(matrix[i][j],"<3"),end="")
    print()
print("Enter the elements of matrix1:")
matrix1=[[int(input()) for i in range (c)] for j in range(r)]
print("matrix1:")
for i in range (r):
    for j in range (c):
        print(format(matrix1 [i][j],"<3"),end="")
    print()
