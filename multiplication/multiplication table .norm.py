def print_multiplication_table(number):
    for i in range(1, number + 1):
        print(f"{i} x {number} = {i * number}")

user_input = input("Enter a number : ")

if user_input.isdigit():
    num = int(user_input)
    print_multiplication_table(num) 
else:
    print("Invalid input. Please enter a positive integer.")
