def print_multiplication_table_with_list(number):
    results = []  
    
    for i in range(1, number + 1):
        result = i * number
        results.append(result) 
        print(f"{i} x {number} = {result}")
    
    return results  

user_input = input("Enter a number : ")

if user_input.isdigit():
    num = int(user_input)
    results = print_multiplication_table_with_list(num)  
   
    print( results)
else:
    print("Invalid input. Please enter a positive integer.")
