from os import system

#codigo de Rodrigo y Elias

def sortbubble (lista_a_comprobar,ls1,ls2,ls3,ls4,ls5):
    #funcion modificada para mover a la par varias listas
    intercambio = True
    while intercambio:
            intercambio = False
            for a in range(len(lista_a_comprobar) - 1):
                if lista_a_comprobar[a]<lista_a_comprobar[a+1]:
                    lista_a_comprobar[a],lista_a_comprobar[a+1]=lista_a_comprobar[a+1],lista_a_comprobar[a]
                    ls1[a],ls1[a+1]=ls1[a+1],ls1[a]
                    ls2[a],ls2[a+1]=ls2[a+1],ls2[a]
                    ls3[a],ls3[a+1]=ls3[a+1],ls3[a]
                    ls4[a],ls4[a+1]=ls4[a+1],ls4[a]
                    ls5[a],ls5[a+1]=ls5[a+1],ls5[a]
                    intercambio=True
    return (lista_a_comprobar,ls1,ls2,ls3,ls4,ls5)

def nombre(mensaje=": "):
    try:
        while True:
            name=input (mensaje)
            name2=name
            name =int (name)
    except ValueError:
        return name2

def frstplce (lista):
    aux_lista =[]
    while True:
        for a in lista:
            if a!=lista[0]:
                b = lista.index (a)
                if lista[b] == lista [0]:
                    aux_lista.append (lista[b+1])
                else: break
            else: aux_lista.append (a)
        break
    return aux_lista

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
    sueldo = float(valor_hora*h_dia) + (valor_hora*h_noche*1.5) + (valor_hora*h_finde*2) + (valor_hora*finde_noche*2.5)
    return (int(sueldo))

texto1= str("ingrese cantidad de horas trabajadas de dia: ")
texto2=str("cantidad de horas trabajadas de noche: ")

v_h= int (0)
trabajador = []
h_trab = []
h_trab_noche = [] 
h_trab_finde = []
h_trab_finde_noche = []
sueldo = []
option = 10

while option !=0:
    #system ("cls")
    print ("1 ingresar valor hora")
    print ("2 ingresar trabajador y horas trabajadas")
    print ("3 listado de trabajadores y sueldo")
    print ("4 listado de trabajadores que tienen mas horas semana noche")
    print ("5 trabajador que tiene mas horas semana dia")
    print ("6 trabajador que tiene mas hora de fin de semana noche")
    print ("0 salir")

    option = leerNumero ("ingrese opcion: ")

    if option == 1: #1 
        v_h = leerNumero ("ingrese el valor de la hora: $")

    elif option == 2: #2 ingresar trabajador y horas trabajadas
        system ("cls")
        trabajador.append (nombre("ingrese nombre del trabajador: "))

        print("durante dias de semana (Lunes a Viernes)")
        h_trab.append (leerNumero (texto1))
        h_trab_noche.append (leerNumero (texto2))
        print ()
        print ("y durante el fin de semana (Sabado y Domingo)")
        h_trab_finde.append (leerNumero (texto1))
        h_trab_finde_noche.append (leerNumero (texto2))    
        sueldo.append (calculo (v_h, h_trab[-1],h_trab_noche[-1],h_trab_finde[-1],h_trab_finde_noche[-1]))

    elif option == 3: #3 listado de trabajadores y sueldo
        system ("cls")
        for a in trabajador:
            b= trabajador.index (a)
            print ( f"{trabajador [b]} gana {sueldo [b]} pesos")

    elif option == 4: #4 listado de trabajadores que tienen mas horas semana noche
        sortbubble (h_trab_noche,trabajador,h_trab,h_trab_finde,h_trab_finde_noche,sueldo)
        for a in frstplce(h_trab_noche):
            b=h_trab_noche.index (a)
            print (f"{trabajador [b]} tiene {h_trab_noche[b]} horas trabajadas")

    elif option == 5: #5 trabajador que tiene mas horas semana dia
        sortbubble (h_trab,trabajador,h_trab_noche,h_trab_finde,h_trab_finde_noche,sueldo)
        for a in frstplce(h_trab):
            b=h_trab.index (a)
            print (f"{trabajador [b]} tiene {h_trab[b]} horas trabajadas")

    elif option == 6: #6 trabajador que tiene mas hora de fin de semana noche
        sortbubble (h_trab_finde_noche,trabajador,h_trab_noche,h_trab_finde,h_trab,sueldo)
        for a in frstplce(h_trab_finde_noche):
            b=h_trab_finde_noche.index (a)
            print (f"{trabajador [b]} tiene {h_trab_finde_noche[b]} horas trabajadas")
    
    elif option == 0: #0 salir
        print ("saliendo ...")

    elif option >=7:
        print ("ingrese una opcion valida")

