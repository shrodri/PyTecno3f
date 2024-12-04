import secrets, string
diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}
letras_Numeros = diccionario['letras'] + diccionario['numeros']
letras_Numeros_Caracteres = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
def soloLetras():
    return ''.join(secrets.choice(diccionario['letras']) for _ in range(8))

def soloNumeros():
    return ''.join(secrets.choice(diccionario['numeros']) for _ in range(8))

def letrasNumeros():
    return ''.join(secrets.choice(letras_Numeros) for _ in range(8))

def letrasNumerosCaracteres():
    return ''.join(secrets.choice(letras_Numeros_Caracteres) for _ in range(8))

def crearPassword():
    tipoPassword = int(input("1:Solo Letras:\n2:Solo numeros:\n3:Letras & Numeros\n4:Letras, Numeros & Caracteres\n\n Por favor, seleccione el tipo de contraseña deseada:    "))
    if tipoPassword == 1:
        password = soloLetras()
        print(f"La contraseña es: {password}")
    elif tipoPassword == 2:
        password = soloNumeros()
        print(f"La contraseña es: {password}")
    elif tipoPassword == 3:
        password = letrasNumeros()
        print(f"La contraseña es: {password}")
    elif tipoPassword == 4:
        password = letrasNumerosCaracteres()
        print(f"La contraseña es: {password}")
    else:
        print("Ingresaste una opcion incorrecta")
        crearPassword()

crearPassword()