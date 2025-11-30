def sum(n):

    return n*(n+1)/2
n = int(input("enter the number:"))
print("sum is", sum(n))

def arraysum(a):
    sum = 0 
    for i in a:
        sum = sum + i

    return(sum)

a = [12, 3, 4, 15]
arraysum(a)
print("arraysum =", arraysum(a))

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("the sum is", summ(n))

