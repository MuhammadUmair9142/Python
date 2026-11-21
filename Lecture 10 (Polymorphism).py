#polymorphism

class Shape:
    def area(self,*args):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

rect = Rectangle()
print(rect.area(5,10))

class Circle(Shape):
    def area(self, pi, r):
        return pi * r**2

cir = Circle()
print(cir.area(3.14,10))