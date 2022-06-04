from os import system
import time
teams = []
points = []
points_sorted = []
puntos = 0
option = 10

while option !=0:
    system ("cls")
    print ("1 ingresar equipo y puntos")
    print ("2 modificar puntaje")
    print ("3 eliminar equipo")
    print ("4 ver tabla de posiciones") #(mas o menos puntos)
    print ("5 ver 3 primeros lugares")
    print ("0 salir")
    print (teams)
    print (points)
    option = int (input ())
    a=0
    b=0
    if option == 1: #1 ingresar equipo y puntos
        teams_name = input ("ingrese el quipo: ")
        if teams_name not in teams:
            teams.append (teams_name)
            points.append (0)
            puntos = int (input ("ingrese puntos: "))
            a= teams.index (teams_name)
            points[a]=puntos
        else: print ("este equipo ya esta en la lista")


    elif option == 2: #2 modificar puntaje
        print ("editar puntos")
        print ("¿como desea editar?")
        print ("1 por indice        2 por nombre")
        a=int(input())
        if a == 1:
            print ("seleccione un número para editar")
            a=1
            for b in teams:
                print (a, b)
                a=a+1
            editar = int(input())
            editar =editar-1
            print (teams[editar])
            points [editar] = int(input("ingrese cantidad: "))
    elif option == 3: #3 eliminar equipo
        print ("¿como desea eliminar?")
        print ("1 por indice        2 por nombre")
        a=int(input())
        if a == 1:
            print ("seleccione un número para eliminar")
            a=1
            for b in teams:
                print (a, b)
                a=a+1
            eliminar = int(input())
            eliminar = eliminar-1
            teams.pop (eliminar)
            points.pop (eliminar)
        elif a == 2:
            a=1
            print ("ingrese el nombre del equipo")
            for b in teams:
                print (a, b)
                a=a+1
                time.sleep (0.4)
            eliminar = str(input())
            teams.remove (eliminar)

    elif option == 4: #4 ver tabla de posiciones (de mas a menos puntos)
        print ("1 sorted, 2 metodo burbuja")
        a =int (input ())
        if a ==1:
            points_sorted = sorted (points, reverse=True)
            for a in points_sorted:
                b = points.index (a)
                print (teams[b], a, "puntos")
            input ()
        elif a ==2:
            for a in points:
                a
    elif option == 5: #5 ver 3 primeros lugares
        a
    elif option == 0: #6 salir
        print ("saliendo ...")

