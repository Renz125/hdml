def totalFlips(number1 , number2):

    flips = 0 
    
    # get the last bit of both numbers and check of both number are the same  if yes no flip required if no a flip is required
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 != t2):
            flips += 1

        number1 >>= 1
        number2 >>= 1

    return flips

number1 = int(input("enter the first number : "))
number2 = int(input("enter the second number : "))

print("\nNumber of flips needed: ", totalFlips(number1, number2))