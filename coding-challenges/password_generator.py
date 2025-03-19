import string
import random

def password_generator(length):
    password = ''
    
    if length < 1 : 
        return "La longitud de la contraseña debe ser mayor a 0"
    
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

new_password = int(input("Ingrese la longitud de su contraseña: "))
print(password_generator(new_password))