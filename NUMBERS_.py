# 1. Odd numbers under the user's input value
limit = int(input("Enter a number: "))

odd_numbers = [num for num in range(limit) if num % 2 != 0]
# Creating a second list of odd numbers (e.g., squares of those odd numbers)
odd_squares = [num**2 for num in odd_numbers]

print("Odd numbers under input:", odd_numbers)
print("Another list of odd numbers (squared):", odd_squares)


# 2. Capitalize the first letter of every fruit in a list
fruits = ["apple", "banana", "cherry", "mango", "orange"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated list of fruits:", capitalized_fruits)
