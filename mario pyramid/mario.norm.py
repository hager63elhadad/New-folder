def print_mario_pyramid(rows):
    for i in range(1, rows + 1):
        
        print(" " * (rows - i) + "*" * i)


user_input = input("Enter the number of rows for Mario's pyramid: ")

if user_input.isdigit():
    rows = int(user_input)
    if rows > 0:
        print_mario_pyramid(rows)
    else:
        print("Please enter a positive integer.")
else:
    print("Invalid input. Please enter a number.")

