import getpass
import string

def check_password_strength(password: str) -> str:
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    if score <= 2:
        return "Weak password"
    elif score in (3, 4):
        return "Moderate password"
    else:
        return "Strong password"

if __name__ == "__main__":
    password = getpass.getpass("Enter password to check: ")  # hides input, never echoed
    print(check_password_strength(password))