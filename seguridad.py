#Rodrigo Chanquey y Leandro Diaz

from os import system
import time
visitantes = ["leandro","rodrigo","leandro","leandro","leandro","leandro","mati","mati","mati","mati","mati","mati","mati","mati"]
ruts = ["5-6","1-2","5-6","5-6","5-6","5-6","3-4","3-4","3-4","3-4","3-4","3-4","3-4","3-4"]
option = 10
rut = "1-1"
while option !=0:
    system ("cls")
    print ("1 ingresar visitantes")
    print ("2 ver a todos los visitantes")
    print ("3 ver los visitantes que han venido mas de cuatro veces")
    print ("4 buscar el visitante por el RUT") 
    print ("0 salir")

    option = int (input ())
    a = 0
    b = 0
    c = 0
    lista = []
    if option == 1: #1 ingresar visitantes
        system ("cls")
        print ("ingrese rut")
        rut = input ()
        print ("ingrese nombre:")
        nombre = input()
        if rut not in ruts:
            ruts.append (rut)
            visitantes.append (nombre)
        else:
            b = ruts.index (rut)
            if visitantes[b]== nombre:
                ruts.append (rut)
                visitantes.append (nombre)
            else:
                print ("la persona está en la lista y el nombre no coincide")
                input()


    elif option == 2: #2 ver a todos los visitantes
        system ("cls")
        for a in visitantes:
            if a not in lista:
                b = visitantes.index (a)
                print ("rut:", ruts[b])
                print ("nombre:", visitantes[b])
                if visitantes.count(a)!=1:
                    print (f"ha venido {visitantes.count (a)} veces")
                else:print (f"ha venido {visitantes.count (a)} vez")
                print ()
                lista.append (a)
        input()

    elif option == 3: #3 ver los visitantes que han venido mas de cuatro veces
        system ("cls")
        for a in ruts:
            c = ruts.index (a)
            b = ruts.count (a)
            if b>4:
                if a not in lista:
                    print (f"{visitantes[c]} ha venido {b} veces")
                    lista.append (a)
        input()




    elif option == 4: #4 buscar el visitante por el RUT, si ha venido mostrar el nombre y cuantas veces ha entrado
        system ("cls")
        print ("ingrese el rut a buscar:")
        a= input ()
        if a in ruts:
            b = ruts.index (a)
            c= visitantes[b]
            if ruts.count(a)!=1:
                print (f"{c} ha venido {ruts.count (a)} veces")
            else:print (f"{c} ha venido {ruts.count (a)} vez")
        input()




    elif option == 0: #0 salir
        print ("saliendo ...")
