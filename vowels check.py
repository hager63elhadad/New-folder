def check_vowels(input_string):
    vowels = "aeiouAEIOU"
    found_vowels = [char for char in input_string if char in vowels]
    return found_vowels


user_input = input("Enter a string: ")

vowels_in_string = check_vowels(user_input) 

print("Vowels found in the string:", vowels_in_string)

