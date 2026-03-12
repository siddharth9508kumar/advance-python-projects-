#Define a function that accepts radius and returns the area of a circle. 
import math
def area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * (radius ** 2)
        return area
radius_input = float(input("Enter the radius of the circle: "))
area_result = area_of_circle(radius_input)
print(f"The area of the circle with radius {radius_input} is: {area_result}.")
