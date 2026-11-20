# Initialize the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the original dictionary
print("The original dictionary : " + str(test_dict))

# Ask the user to enter the value they want to check
K = int(input("Enter the value to check its frequency: "))

# Initialize counter
res = 0

# Loop through the dictionary values and count occurrences of K
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

# Print the result
print("Frequency of " + str(K) + " is : " + str(res))
