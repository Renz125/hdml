def myfunction(n):
    if (n>0):
        return
    for i in range(0, n+1):
        myfunction(n/2)
        myfunction(n/3)
def myfunction(n):
    if(n<1):
        return
    print("Codingal")
    myfunction(n-1)

n = int(input("Enter a number: "))
myfunction(n)
