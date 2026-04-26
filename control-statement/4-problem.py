# Write a  program to input sides of a triangle and check whether a triangle is equilateral, scalene or isosceles triangle.

side1, side2, side3 = map(int, input("Enter the side1, side2, side3 : ").split())

if side1  == side2 == side3:
    print("Equilateral Triangle")
elif side1 != (side2 and side3) and side2 != (side1 and side3) and side3 != (side1 and side2):
    print("Scalene triangle")
else:
    print("Isosceles triangle")