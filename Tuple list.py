my_tuple = ("Albert","Pennywise",24,"167cm", "74kg","Science")
print(my_tuple)

set1 = {"Albert","Pennywise","Science"}
set2 = {24,"167cm", "74kg"}

print("Original Sets:")
print("Set 1:",set1)
print("Set 2:",set2)

print("Union")
set3 = set1.union(set2)
print(set3)
#diff kind of intersections/p.s just diff symbols

print("Intersection")
set4=set1.intersection(set2)
print(set4)

union_set = set1 | set2
print("Union:",union_set)

Intersection_set = set1 & set2
print("Union:",Intersection_set)