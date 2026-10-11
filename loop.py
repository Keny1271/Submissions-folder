
number = int(input("Enter a number: "))
original_number = number
number = abs(number)
digit_count = 0
if number == 0:
    digit_count = 1
else:
    while number > 0:
        digit_count += 1
        number = number // 10
print(f"The total number of digits in {original_number} is: {digit_count}")
