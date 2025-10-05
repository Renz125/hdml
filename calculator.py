def add(num1,num2):
    return num1 + num2 

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2



num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))

print("Sum:", add(num1,num2))
print("Difference:", subtract(num1,num2)) 
print("Multiplication:", multiply(num1,num2))
print("Division:", divide(num1,num2))  