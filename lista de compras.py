from os import system
from re import A
from subprocess import list2cmdline
import time
system ("cls")
lista_de_compras = []
cantidad = []

option = 0


while option !=5 :
    system ("cls")

    print ("1 agregar productos a tu lista de compra")
    print ("2 mostrar tu lista de compras")
    print ("3 remover elementos")
    print ("4 editar cantidad")
    print ("5 salir")
    a=0
    b=0
    option = int(input("ingrese opcion: "))

    if option == 1:
        print ("agregar productos a tu lista de compra")
        producto= input()


        if producto not in lista_de_compras:
            lista_de_compras.append (producto)
            cantidad.append (int(1))
        else:
            b = lista_de_compras.index (producto)
            cantidad[b]= cantidad[b] + 1


    elif option ==2:
        print ("tu lista de compras:")
        for a in lista_de_compras:
            b = lista_de_compras.index (a)
            print (lista_de_compras[b], cantidad[b])
        time.sleep (2)
    elif option == 3:
        system("cls")
        print ("¿como desea eliminar?")
        print ("1 por indice        2 por nombre")
        a=int(input())
        if a == 1:
            print ("seleccione un número para eliminar")
            a=1
            for variable in lista_de_compras:
                print (a, variable)
                a=a+1
            eliminar = int(input())
            eliminar =eliminar-1
            lista_de_compras.pop (eliminar)
        elif a==2:
            a=1
            print ("ingrese el nombre del producto")
            for variable in lista_de_compras:
                print (a, variable)
                a=a+1
            eliminar = str(input())
            lista_de_compras.remove (eliminar)
    elif option == 4:
        print ("editar cantidad")
        print ("¿como desea editar?")
        print ("1 por indice        2 por nombre")
        a=int(input())
        if a == 1:
            print ("seleccione un número para editar")
            a=1
            for variable in lista_de_compras:
                print (a, variable)
                a=a+1
            editar = int(input())
            editar =editar-1
            print (lista_de_compras[editar])
            cantidad [editar] = int(input("ingrese cantidad: "))
        elif a==2:
            a=1
            print ("ingrese el nombre del producto")
            for a in lista_de_compras:
                b = lista_de_compras.index (a)
                print (lista_de_compras[b], producto[b])
            editar = str(input())
            #lista_de_compras.remove (editar)

    elif option == 5:
        print ("saliendo ...")
