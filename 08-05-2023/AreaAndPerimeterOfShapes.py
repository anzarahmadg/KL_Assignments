import math

class Triangle:
    def calculate_area(side1, side2):
        area = (side1 * side2)*0.5
        return area
    def calculate_perimeter(side1, side2, side3):
        return side1 + side2 + side3

class Circle:
    def areaOfCircle(r):
        return 3.14*(r*r)
    def perimeterOfCircle(r):
        return 2*3.14*r

class Rectangle:
    def areaOfRectangle(length, breadth):
        return length * breadth
    def peremeterOfRectangle(length, breadth):
        return 2*(length+breadth)

class Square:
    def areaOfSquare(side):
        return side * side
    def peremeterOfSquare(side):
        return 4*side
    
while True:
    shape = int(input("Press \n 1 for Triangle \n 2 for Circle \n 3 for Rectangle \n 4 for Square \n 5 to quit \n  "))
    if shape == 1:
        side1 = float(input("Enter the base of triangle: "))
        side2 = float(input("Enter the height of triangle: "))
        side3 = float(input("Enter the length of side 3: "))
        print(Triangle.calculate_area(side1,side2))
        print(Triangle.calculate_perimeter(side1,side2,side3))

    elif shape == 2:
        radius = float(input("Enter the radius of Circle: "))
        print(Circle.areaOfCircle(radius))
        print(Circle.perimeterOfCircle(radius))

    elif shape == 3:
        length = int(input("Enter the Length of Rectangle: "))
        breadth = int(input("Enter the breadth of Rectangle: "))
        print(Rectangle.areaOfRectangle(length,breadth))
        print(Rectangle.peremeterOfRectangle(length,breadth))

    elif shape == 4:
        side = int(input("Enter the side of Square: "))
        print(Square.areaOfSquare(side))
        print(Square.peremeterOfSquare(side))

    elif shape == 5:
        exit()
    
    else:
        print("invalid input")