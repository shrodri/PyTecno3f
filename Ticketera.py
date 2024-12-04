
import pickle, sys, os, random
ticketera = {}
archivo_ticketera = "baseDeTickets"

with open("baseDeTickets", "wb") as f:
        pickle.dump(ticketera, f)

with open("baseDeTickets", "rb") as f:
        ticketera = pickle.load(f)


def crearTicket ():
            print("Ingrese los datos para crear su ticket:  ")
            nombre = input("Ingrese su nombre de usuario:   ")
            sector = input("Ingrese el sector al que pertenece:    ")
            asunto = input("Ingrese el asunto del ticket:   ")
            mensaje = input("Ingrese un mensaje:    ")
            nroTicket = random.randrange(1000, 9999)
            while nroTicket in ticketera:
                nroTicket = random.randrange(1000, 9999)
            ticketera[nroTicket] = {'nombre': nombre,'sector': sector,'asunto': asunto,'mensaje': mensaje}            
            print (f"Se ha generado el siguiente ticket :\n Su nombre:   {nombre}   Nro de Ticket:   {nroTicket}\n Sector:   {sector}\n Asunto:  {asunto}\n Mensaje: {mensaje}\n    Por favor recuerde el numero de ticket ")
            opcion2 = input("Desea crear otro ticket? (s/n):   ")
            if opcion2 == "s":
                crearTicket()
            elif opcion2 == "n" :
                menu()  
def leerTicket ():
        nroTicketLeer = int(input("Por favor, ingrese el numero de ticket a leer:   "))
        for nroTicket in ticketera.items():
             if nroTicket == nroTicketLeer:
                print(f"Informacion del ticket:\n  Nombre: {ticketera[nroTicketLeer]['nombre']}\n  Sector:  {ticketera[nroTicketLeer]['sector']}\n Asunto: {ticketera[nroTicketLeer]['asunto']}\n  Mensaje:    {ticketera[nroTicketLeer]['mensaje']}\n")   
                opcion3 = input("Quisiera leer otro ticket? Caso contrario , se regresara al menu principal (s/n):  ")
                if opcion3 == "s":
                    leerTicket()
                elif opcion3 == "n" :
                    menu()
        else:
            print("El numero ingresado es erroneo.")
            menu()
def menu():
    opcionMenuPrincipal = int(input("Bienvenido al sistema de tickets\n Ingrese la opcion deseada \n 1 - Generar un nuevo Ticket \n 2 - Leer un Ticket \n 3 - Salir \n Seleccione:  " ))
    if opcionMenuPrincipal == 1:
        crearTicket()        
    elif opcionMenuPrincipal == 2:
        leerTicket()   
    elif opcionMenuPrincipal == 3:
        print("Saliendo del programa")
        sys.exit()

menu()