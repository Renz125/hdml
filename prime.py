number = int(input("enter a number:"))
if number > 1:
        for i in range(2,int(number**0.5)+1):
                if number % i == 0:
                    print(number,"is not prime")
                    break
        else:
            print(number,"is  prime")
else:
    print(number,"is not  prime")