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
        return self.side ** 3.16

class Octangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 2.7 * self.base * self.height
    
class Diamond(Polygon):
    def __init__(self, corners, width):
        self.corners = corners
        self.width = width
        
    def area(self):
        return 15 * self.corners * self.width
    
rec = Rectangle(99, 2000)
squ = Square(600)
oct = Octangle(30, 60)  
dia = Diamond(21, 67)     

for shape in(rec, squ, oct, dia):
    print(f"The area of {shape.__class__.__name__} is  {shape.area()}")