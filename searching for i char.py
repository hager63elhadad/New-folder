def search_for_i(input_string):
    
    indices = [index for index, char in enumerate(input_string.lower()) if char == 'i']
    return indices

user_input = input("Enter a string : ")


indices_of_i = search_for_i(user_input)

if indices_of_i:
    print(f"The indices are: {indices_of_i}")
else:
    print("The letter 'i' does not appear in the string.")

