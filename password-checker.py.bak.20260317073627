def check_password_strength(password: str) -> None:
    """
    Prints a message indicating whether the given password is strong or weak.

    A password is considered strong if it has at least 8 characters.

    Args:
        password (str): The password to check.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if len(password) < 8:
        print("Weak password")
    else:
        print("Strong password")

# Example usage:
password = "mypassword123"
check_password_strength(password)
```

Or, using a more concise approach:

```python
def check_password_strength(password: str) -> None:
    """
    Prints a message indicating whether the given password is strong or weak.

    A password is considered strong if it has at least 8 characters.

    Args:
        password (str): The password to check.
    """
    if not isinstance(password, str) or len(password) < 8:
        print("Weak password")
    else:
        print("Strong password")

# Example usage:
password = "mypassword123"
check_password_strength(password)