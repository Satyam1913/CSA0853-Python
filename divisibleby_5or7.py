def divisible(n):
    for j in range(1, n+1):
        if j % 5 == 0 or j % 7 == 0:
            yield j
if __name__ == "__main__":
    N = 50
    for j in divisible(N):
        print(j, end = " ")
        print()
