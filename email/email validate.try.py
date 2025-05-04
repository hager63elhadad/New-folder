def validate_input():
    while True:
        try:
            username = input("Enter a username: ")
            if username.isdigit():
                raise ValueError("Username cannot be all digits.")
            if len(username.strip()) == 0:
                raise ValueError("Username cannot be empty.")

            email = input("Enter your email: ")
            if '@' not in email or '.' not in email:
                raise ValueError("invailed email")

            at_index = email.find('@')
            dot_index = email.find('.', at_index)

            if at_index <= 0:
                raise ValueError("invailed email")
            if dot_index == -1 or dot_index - at_index <= 1:
                raise ValueError("invailed email")
            if email.endswith('@') or email.endswith('.'):
                raise ValueError("invailed email")

            print("Username and Email are valid!")
            break

        except ValueError as ve:
            print("Validation error:", ve)

validate_input()
