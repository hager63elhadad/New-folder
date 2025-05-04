def mario_pyramid(height):
    if not isinstance(height, int) or height <= 0:
        print("Height must be a positive integer.")
        return

    pyramid = [] 
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        blocks = '#' * i
        row = spaces + blocks
        pyramid.append(row)

    
    for line in pyramid:
        print(line)


user_input = input("Enter the height for Mario's pyramid: ")

if user_input.isdigit():
    height = int(user_input)
    mario_pyramid(height)  
else:
    print("Invalid input. Please enter a positive integer.")
