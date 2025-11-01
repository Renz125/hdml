class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a  cat, my name is {self.name} and my age is {self.age}")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog, my name is  {self.name} ans my age is {self.age}")

    def make_sound(self):
        print("Woof")

cat1 = Cat("Martin", 3.5)
dog1 = Dog("Noli", 9)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()