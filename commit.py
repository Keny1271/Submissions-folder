def square_and_filter(start, end):
    # Create lists to store the squared values
    even_squares = []
    odd_squares = []
    
    # Loop through the range of numbers (inclusive of end)
    for num in range(start, end + 1):
        square = num ** 2
        
        # Filter into even or odd lists
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    # Print the results
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

# Example usage:
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

square_and_filter(start_num, end_num)
