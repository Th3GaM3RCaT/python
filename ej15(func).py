from os import system
import random
def sumae(n_inic):
    n_a_uni = []
    mod = 10
    inic= n_inic
    condi=True
    while condi:
        if inic!=0:
            uni = inic % mod 
            n_a_uni.append (uni) 
            dec = inic - uni 
            sig_uni = int(dec/mod) 
        else:condi=False
        inic = sig_uni 
    b=int(0)
    for a in n_a_uni:
        b=b+a
    return(b)

system ("cls")
lista=[]
lista2 = []
print ("lista aleatoria de 10 numeros entre 1 y 100")
for a in range (10):
    lista.append (random.randint(1,100))
for a in lista:
    print (a)
    b=sumae(a)
    lista2.append(b)
c=max (lista2)
d= lista2.index(c)
print (f"el numero que da un numero mayor es {lista[d]} dando {lista2[d]} ")
