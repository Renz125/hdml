def powerof4(number):

    count = 0

    #if only 1 set bit exists
    if(number &(~(number &( number - 1)))):

        while(number > 1):
            number >>= 1
            count += 1
        
        # If count is even return true if not/else return false
        if(count % 2 == 0):
            return True
        else:
            return False
        
number = int(input("Enter a number: "))

if (powerof4(number)):
        print("\nThe number is the a power of 4")
else:
        print("\nThe number is not a power of 4")