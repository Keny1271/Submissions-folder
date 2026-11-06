try:
    # Take user input and immediately try to convert it into a whole number
    age_input = input("Please enter your age: ")
    age = int(age_input)
    
    # If successful, check if the age is even or odd
    if age % 2 == 0:
        print(f"The entered age ({age}) is an Even number.")
    else:
        print(f"The entered age ({age}) is an Odd number.")

except ValueError:
    # This block triggers if int() fails (e.g., for letters, decimals, or symbols)
    print("Value Error: Please enter a valid integer (whole number).")
