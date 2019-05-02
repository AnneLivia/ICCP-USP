from random import randint

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(randint(0,1000))
    return lista
