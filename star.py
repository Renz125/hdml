print(" star pattern")
n=int(input("enter the limit"))
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()
