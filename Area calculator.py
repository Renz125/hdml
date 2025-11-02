class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
rec = Rectangle(60, 90)
squ = Square(20)
tri = Triangle(60, 70)       

for shape in(rec, squ, tri):
    print(f"The area of {shape.__class__.__name__} is  {shape.area()}")