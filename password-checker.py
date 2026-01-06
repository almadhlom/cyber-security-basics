# Simple password strength checker
password = "mypassword123"
if len(password) < 8:
    print("Weak password")
else:
    print("Strong password")

# simple password strength checker

password = "mypassword123"

for index, char in enumerate(password):
    print(f"Index {index}: {char}")

if len(password) < 8:
    print("weak password")
else:
    print("strong password")
