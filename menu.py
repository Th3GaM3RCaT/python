from os import system
import time

option = 10

while option !=0:
    system ("cls")
    print ("1 ")
    print ("2 ")
    print ("3 ")
    print ("4 ") #(mas o menos puntos)
    print ("5 ")
    print ("0 salir")
    try:
        option = int (input ())
        a = 0
        b = 0
        if option == 1: #1 
            print ("opcion 1")
            print (f"a es {a} ")
            time.sleep (1)

        elif option == 2: #2 
            print ("opcion 2")

        elif option == 3: #3 
            print ("opcion 3")

        elif option == 4: #4 
            print ("opcion 4")

        elif option == 5: #5 
            print ("opcion 5")

        elif option == 0: #0 salir
            print ("saliendo ...")
    except ValueError:
        print ("mejor ingrese un número")

