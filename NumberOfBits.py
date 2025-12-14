def NumberofBits(n):

    count = 0

    while (n):
        count += 1
        n >>= 1

    return count

number = int(input("Enter a Number: "))
print("The total number of bits:", NumberofBits(number)) 