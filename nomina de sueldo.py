from os import system


def menu():
    print ("1 ingresar valor hora")
    print ("2 ingresar trabajador y horas trabajadas")
    print ("3 listado de trabajadores y sueldo")
    print ("4 listado de trabajadores que tienen mas horas semana noche")
    print ("5 trabajador que tiene mas horas semana dia")
    print ("6 trabajador que tiene mas hora de fin de semana noche")
    print ("0 salir")

def leerNumero(mensaje, mensaje_error= "Formato numero incorrecto "):
    leido = False
    num = 0
    while not leido:
        try:
            num = int(input(mensaje))
            leido = True
        except ValueError:
            print(mensaje_error)
    return num

def calculo(valor_hora, h_dia, h_noche, h_finde, finde_noche):

    h_dia = (valor_hora*1)*h_dia
    h_noche = (valor_hora*1.5)*h_noche
    h_finde =(valor_hora*2)*h_finde
    finde_noche = (valor_hora*2.5)*h_finde

    sueldo = h_dia + h_finde + h_noche + finde_noche

    return (sueldo)

v_h= int (0)
trab = []
h_trab = []
h_trab_noche = []
h_trab_finde = []
h_trab_finde_noche = []
sueldo = []
option = 10
while option !=0:
    #system ("cls")
    menu()
    print (v_h)
    option = leerNumero ("ingrese opcion: ")
    if option == 1: #1 
        v_h = leerNumero ("ingrese el valor de la hora: $")

    elif option == 2: #2 ingresar trabajador y horas trabajadas
        system ("cls")
        trab.append (str (input ("ingrese nombre del trabajador: ")))

        print("durante dias de semana (Lunes, Martes, Miercoles, Jueves, Viernes)")
        h_trab.append (leerNumero ("ingrese cantidad de horas trabajadas de dia: "))
        h_trab_noche.append(leerNumero ("cantidad de horas trabajadas de noche:"))

        print ("y durante el fin de semana (Sabado, Domingo)")
        h_trab_finde.append (leerNumero ("cantidad de horas trabajadas de dia: "))
        h_trab_finde_noche.append (leerNumero ("cantidad de horas trabajadas de noche: "))

        for a in range (len (trab)):
            sueldo.append (calculo (v_h,h_trab[a],h_trab_noche [a], h_trab_finde [a], h_trab_finde_noche [a]))


    elif option == 3: #3 listado de trabajadores y sueldo
        system ("cls")
        print ("opcion 3")
        for a in range (len (trab)):
            print ( f"{trab[a]} gana {sueldo[a]}")

    elif option == 4: #4 listado de trabajadores que tienen mas horas semana noche
        print ("opcion 4")

    elif option == 5: #5 trabajador que tiene mas horas semana dia
        print ("opcion 5")

    elif option == 6: #6 trabajador que tiene mas hora de fin de semana noche
        print ("opcion 6")
    
    elif option == 0: #0 salir
        print ("saliendo ...")


