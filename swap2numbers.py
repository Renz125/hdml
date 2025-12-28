def swap1(a, b):
    
    a = a ^ b
    b = a ^ b
    c = a ^ b
    print("after swapping the first batch: a =", a, " b =", b)

def swap2(a,b):

    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("after swapping the second batch: a =", a, "b =", b)

swap1 (1,2)
swap2 (1,2)

