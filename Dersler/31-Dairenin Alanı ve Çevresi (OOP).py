class Circle:
    pi = 3.14
    def __init__(self,r = 1): # If constructor doesn't take parameter, r automatically be 1.
        self.radius = r
    def calculateArea(self):
        return (self.pi*(self.radius**2))
    def calculatePerimeter(self):
        return (2*self.pi*self.radius)

c1 = Circle() # c1.radius = 1
c2 = Circle(5)

print(f"Area of c1 is {c1.calculateArea()}, perimeter of c1 is {c1.calculatePerimeter()}")
print(f"Area of c2 is {c2.calculateArea()}, perimeter of c2 is {c2.calculatePerimeter()}")