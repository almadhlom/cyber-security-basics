def check_password_strength(passwords):
    for i, password in enumerate(passwords):
        if len(password) < 8:
            print(f"Password {i} is too weak.")
        elif not any(char.isdigit() for char in password):
            print(f"Password {i} needs a number.")
        else:
            print(f"Password {i} is strong.")