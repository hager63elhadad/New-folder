def validate_input():
    while True:
        errors = []  

        username = input("Enter a username: ").strip()
        email = input("Enter your email: ").strip()

        
        if not username:
            errors.append("Username cannot be empty.")
        if username.isdigit():
            errors.append("Username cannot be all digits.")


        if '@' not in email or '.' not in email:
            errors.append("invailed email")
        else:
            at_index = email.find('@')
            dot_index = email.find('.', at_index)

            if at_index <= 0:
                errors.append("invailed email.")
            if dot_index == -1:
                errors.append("invailed email.")
            elif dot_index - at_index <= 1:
                errors.append("invailed email.")
            if email.endswith('@') or email.endswith('.'):
                errors.append("invailed email")

    
        if errors:
            print("\nValidation errors:")
            for error in errors:
                print("-", error)
            print()
        else:
            print("\nUsername and Email are valid!")
            break

validate_input()

    
