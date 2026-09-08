#Password Strength Checker
# At least 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character

password = input("Enter a password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    print("Password is strong.")

if not any (char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")

if not any (char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")

if not any (char.isdigit() for char in password):
    print("Password must contain at least one digit.")

if not any (char in "!@#$%^&*()-+" for char in password):
    print("Password must contain at least one special character.")
    