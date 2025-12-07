binary = input("Enter a binary Number: ")

decimal = 0
for digit in binary:
    decimal = decimal * 2 + (ord(digit) - ord('0')) 

print(decimal)