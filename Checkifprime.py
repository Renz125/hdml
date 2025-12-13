from math import sqrt

number = int(input("Enter your number:"))
print("\n")

#if given number is greater than 1
if number > 1:

    # To check whether the number is divisible by 2 and tell that number is not a prime
    for i in range(2, int(sqrt(number)+1)):

        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    
    else:
        print(number, "is a prime number")


