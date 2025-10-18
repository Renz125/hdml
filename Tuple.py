#empty
my_tuple = ()
print(my_tuple)

#Integers
my_tuple = (1,2,3)
print(my_tuple)

#Mixed Data
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

my_tuple = ('p', 'e', 'r', 'm','i', 't')
print(my_tuple[0])
print(my_tuple[5])
#nested data types

my_tuple = ("mouse", (1,2,3), [3,2,4])

print(my_tuple[0][4])
print(my_tuple[1][1])

print("Sliced", my_tuple[1:4])

for letter in (my_tuple):
    print("Hello", letter)