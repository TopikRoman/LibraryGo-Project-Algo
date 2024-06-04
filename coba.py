import random
import string

def generate_password():
    characters = string.digits + string.ascii_letters
    password = ""
    for _ in range(8):
        password += random.choice(characters)
    return password

password = generate_password()
print(password)