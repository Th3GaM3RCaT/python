#Rodrigo Chanquey y Leandro Diaz

from os import system
import time
visitantes = ["leandro","rodrigo","leandro","leandro","leandro","leandro"]
ruts = ["5-6","1-2","5-6","5-6","5-6","5-6"]
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
    if option == 1: #1 ingresar visitantes
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
        print ("opcion 2")
        for a in visitantes:
            b = visitantes.index (a)
            print ("rut:", ruts[b])
            print ("nombre:", visitantes[b])
            print ()
        input()

    elif option == 3: #3 ver los visitantes que han venido mas de cuatro veces
        print ("opcion 3")
        lista =[]
        for a in ruts:
            c = ruts.index (a)
            b = ruts.count (a)
            if b>=4:
                if a not in lista:
                    print (f"{visitantes[c]} ha venido {b} veces")
                    lista.append (a)
                    print ("a^3")
                else:
                    print ("a^2")
            else:
                print ("a")
        input()




    elif option == 4: #4 buscar el visitante por el RUT, si ha venido mostrar el nombre y cuantas veces ha entrado
        print ("ingrese el rut a buscar:")
        a= input ()
        if a in ruts:
            b = ruts.index (a)
            print (visitantes[b])
            print (visitantes.count (visitantes[b]))
        input()




    elif option == 0: #0 salir
        print ("saliendo ...")
