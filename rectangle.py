#objects and classes: a program that finds the area of a rectangle and teh perimeter with predefined inputs

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        a= self.length*self.width
        return f"the area is {a}"
    
    def perimeter(self):
        p =(2*self.length)+(2*self.width)
        return f"the perimeter is {p}"
    
shape = Rectangle(20,10)
print(shape.area())
print(shape.perimeter())
