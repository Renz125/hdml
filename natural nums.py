# sum of natural numbers
n = int(input("enter the limit:"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
    print("sum =",sum)
print("the sum of",n,"natural number is" ,sum)