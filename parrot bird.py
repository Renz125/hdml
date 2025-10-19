class parrot:

    species = "bird"

    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    

drew = parrot("drew", 20)
lapi = parrot("lapi", 40)

print("drew is a", drew.species)
print("lapi is a", lapi.species)

print(drew.name, "is", drew.age, "years old")
print(lapi.name, "is", lapi.age, "years old")   