number = int(input("Input your number: "))

digits = len(str(number))

resultNumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** 3
    temp //= 10

if number == resultNumber:
    print(number, "is an armstrong number")
else:
    print(number, " is not an armstrong number")

