import random
from unicodedata import name

def frstplce (n_lista):
    aux_lista =[]
    while True:
        for a in range (len (n_lista)-1):
            if n_lista[0] == n_lista [a+1]:
                aux_lista.append (n_lista[a+1])
            else: break
        break
    if len (aux_lista) >= 1:
        return aux_lista
    else: return n_lista[0]

def sortbubble (lista):
    intercambio = True
    while intercambio:
            intercambio = False
            for a in range(len(lista) - 1):
                if lista[a]<lista[a+1]:
                    lista[a],lista[a+1]=lista[a+1],lista[a]
                    intercambio=True
    return (lista)

lista = []
'''
for a in range (30):
    lista.append (random.randint (0,10))
sortbubble (lista)
print (frstplce(lista))
'''

def nombre(mensaje=": "):
    try:
        while True:
            name=input (mensaje)
            name2=name
            name =int (name)
            
    except ValueError:
        return name2

uwu=nombre("ingresa un nombre: ")


print (uwu)
