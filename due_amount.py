def calculate_change(bill_amount, paid_amount):
    # Calculate the money to be returned
    change_owed = paid_amount - bill_amount
    
    # Return the result back to where the function was called
    return change_owed

# Input values from the story
total_bill = 2.50
amount_paid = 4.00

# Call the function and store the result
vishals_change = calculate_change(total_bill, amount_paid)

# Print the result
print(f"The shopkeeper should return: ${vishals_change:.2f}")
