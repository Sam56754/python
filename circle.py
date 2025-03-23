# pythn coding
import math
try:
    radius = float(input("Enter the radius:"))
    if radius <= 0:
        print("enter a valid number")
        exit()
    class circle:
        def __init__(self, radius):
            self.radius = radius
    
        def getArea(self):
            area = math.pi * math.pow((self.radius),2)
            return f"the area is {area:.2f}"
    
        def getCircumfrence(self):
            cicumfrence = 2*math.pi*(2*self.radius)
            return f"the circimfrence is {cicumfrence:.2f}"
    cat = circle(radius)
    print(cat.getArea())
    print(cat.getCircumfrence())
except ValueError:
    print("please enter a value")
