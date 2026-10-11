
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))
result = 1
if exponent < 0:
    print("Please enter a non-negative exponent for this basic loop program.")
else:
    for _ in range(exponent):
        result *= base


    print(f"{base} raised to the power of {exponent} is: {result}")
