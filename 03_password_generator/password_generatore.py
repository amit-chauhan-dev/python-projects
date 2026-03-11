import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

character = string.ascii_letters + string.digits + string.punctuation

password = " "

for i in range(length):
    password += random.choice(character)

print("Generated Password:", password)