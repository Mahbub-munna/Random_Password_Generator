import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if not pool:
        return "No character sets selected."

    password = [random.choice(pool) for _ in range(length)]
    return "".join(password)

length = int(input("Enter password length: "))
use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

print("Your generated password is:", generate_password(length, use_lower, use_upper, use_digits, use_symbols))
