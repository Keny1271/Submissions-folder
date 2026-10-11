import math
def calculate_circumference(radius):
    """
    Takes the radius of a circle and returns its circumference.
    Formula: 2 * pi * radius
    """
    circumference = 2 * math.pi * radius
    return circumference
user_radius = float(input("Enter the radius of the circle: "))
if user_radius < 0:
    print("Radius cannot be negative.")
else:
    result = calculate_circumference(user_radius)
    print(f"The circumference of the circle is: {round(result, 2)}")
