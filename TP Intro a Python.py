
def calculadora_notas ():
    suma = 0
    cantidad_notas = 0
    nota = float(input("Por favor, ingrese una nota,si ya no hay mas calificaciones, ingrese -1 "))
    while nota  != -1:
        suma = suma + nota
        cantidad_notas = cantidad_notas + 1
        nota = float(input("Por favor, ingrese una nota,si ya no hay mas calificaciones, ingrese -1 "))
    else:
        promedio = suma / cantidad_notas
        print(f"El promedio es {promedio}")
        return promedio      
#calculadora_notas()

def colores_primarios(color):
    if color == "rojo" or color == "amarillo" or color =="azul":
        print(f"El color {color} es primario")
    else:
        print(f"El color ingresado, {color}, no es primario")
    return colores_primarios
#colores_primarios("rojo")

def numero_mayor():
    numero = 0
    numero_alto = 0
    opcion = "s"
    while opcion != "n":
        numero = float(input("Por favor, ingrese un numero:  "))
        opcion = input("Desea agregar otro numero? s/n: ")
        if numero > numero_alto:
            numero_alto = numero
    else:
        print(f"El numero mas alto que se ingreso es : {numero_alto}")
        return numero_alto  
#numero_mayor()

def rectangulo(filas,columnas):
    filas = int(input("Por favor, ingrese el numero de filas:   "))
    columnas = int(input("Por favor, ingrese el numero de columnas: "))
    for i in range (filas):
        print("_"*columnas)
#rectangulo(8,9)

def factorial():
    numero_entero_positivo = int(input("Por favor, ingrese un numero entero positivo"))
    for i in range (0,numero_entero_positivo,1):
        resultado = numero_entero_positivo * i
    print(f"El factorial de {numero_entero_positivo} es {resultado}")
#factorial()