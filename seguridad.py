#from re import X

#el sistema de seguridad de una empresa busca registrar los visitantes 
#para lo cual registra el nombre y el RUT de cada visitante
#la lista puede contener RUT repetidos que corresponden a personas que visitaron
#las instalaciones  mas de una vez
#escriba un programa que permita ingresar los rut de los visitantes 
#y muestre el reporte descrito

#ingresar visitantes
#ver a todos los visitantes
#ver los visitantes que han venido mas de cuatro veces
#buscar el visitante por el RUT, si ha venido mostrar el nombre y cuantas veces ha entrado

from os import system
import time
visitantes = []
rutes = []
option = 10
rut = int (1-1)
while option !=0:
    system ("cls")
    print ("1 ingresar visitantes")
    print ("2 ver a todos los visitantes")
    print ("3 ver los visitantes que han venido mas de cuatro veces")
    print ("4 buscar el visitante por el RUT, si ha venido mostrar el nombre y cuantas veces ha entrado") 
    print ("0 salir")
    try:
        option = int (input ())
        a = 0
        b = 0
        if option == 1: #1 ingresar visitantes
            print ("ingrese rut")
            rut = input ()
            print ("ingrese nombre:")
            nombre = input()
            if rut not in rutes:
                rutes.append (rut)
                visitantes.append (nombre)
            else:
                b = rutes.index[rut]
                if visitantes[b]== nombre:
                    rut.append (rut)
                    visitantes.append (nombre)
                else:
                    print ("la persona está en la lista y el nombre no coincide")


        elif option == 2: #2 ver a todos los visitantes
            print ("opcion 2")
            for a in range (len(visitantes)):
                print ("rut:", rut[a])
                print ("nombre:", visitantes[a])
                print ()

        elif option == 3: #3 ver los visitantes que han venido mas de cuatro veces
            print ("opcion 3")


        elif option == 4: #4 buscar el visitante por el RUT, si ha venido mostrar el nombre y cuantas veces ha entrado
            print ("ingrese el rut a buscar:")
            a= input ()
            if a in rutes:
                b= rutes.index[a]
                print (visitantes[b])
                print (visitantes.count (visitantes[b]))



        elif option == 0: #0 salir
            print ("saliendo ...")
    except ValueError:
        print ("mejor ingrese un número")
