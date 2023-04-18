import random
import string

def generate_password(length=12):
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters
    caracteres_invalidos = ".,\"'/;"
    for char in caracteres_invalidos:
        caracteres_validos = caracteres_validos.replace(char, '')
    password = ''.join(random.choice(caracteres_validos) for i in range(length))
    return password

print(generate_password())