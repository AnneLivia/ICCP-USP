def ordenada(lista):
    orded = True
    for i in range(1,len(lista)):
        if(lista[i - 1] > lista[i]):
            orded = False
    return orded

def main():
    lista1 = [1,2,3,4,5,6]
    lista2 = [9,3,11,35,31,4]
    print(lista1," is orded: ", ordenada(lista1))
    print(lista2," is orded: ", ordenada(lista2))
