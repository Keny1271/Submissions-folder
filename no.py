
char = input("Enter a character: ")
if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
