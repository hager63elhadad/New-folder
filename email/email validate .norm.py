def validate_email(email):
    email = email.strip()

    if email == "" or email.count("@") != 1:
        print("Invalid email.")
        return

    at = email.find("@")

    if at == 0 or at == len(email) - 1:
        print("Invalid email.")
        return

    if "." not in email[at + 1:]:
        print("Invalid email.")
        return

    if email[at + 1] == "." or email[-1] == ".":
        print("Invalid email.")
        return

    if ".." in email[at + 1:]:
        print("Invalid email.")
        return

    print("The email is valid.")



username = input("Enter your username: ").strip()
email = input("Enter your email: ").strip()

print(f"Hello, {username}!")
validate_email(email)

