import string
import random

def password_generator(length):
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

new_password = int(input("Ingrese la longitud de su contraseña: "))
print(password_generator(new_password))