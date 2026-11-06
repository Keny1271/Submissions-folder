import math

def calculate_trig_values(degrees):
    # Convert degrees to radians
    radians = math.radians(degrees)
    
    # Calculate main trigonometric values
    sine_val = math.sin(radians)
    cosine_val = math.cos(radians)
    
    # Tangent is undefined at odd multiples of 90 degrees
    if degrees % 180 == 90:
        tangent_val = "Undefined"
    else:
        tangent_val = math.tan(radians)
        
    print(f"Trigonometric values for {degrees}°:")
    print(f"  • sin({degrees}°) = {sine_val}")
    print(f"  • cos({degrees}°) = {cosine_val}")
    print(f"  • tan({degrees}°) = {tangent_val}")

# Example usage: Find the values for a 45-degree angle
calculate_trig_values(45)
