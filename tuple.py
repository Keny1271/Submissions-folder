# Function to calculate the product of all numbers in a tuple
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

# Given tuples from the problem
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Printing the results
print("Original Tuple 1:", tup1)
print("Product of Tuple 1:", mutiple_tuple(tup1))

print("\nOriginal Tuple 2:", tup2)
print("Product of Tuple 2:", mutiple_tuple(tup2))
