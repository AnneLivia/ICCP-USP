def remove_repetidos(lista):
    clone = lista[:]
    tam = len(clone)
    for elemento in lista:
        cont = 0
        index = 0
        while index < tam:
            if clone[index] == elemento:
                cont = cont + 1
            if(cont >= 2):
                cont = 0
                del(clone[index])
            tam = len(clone)
            index = index + 1
    return sorted(clone)

lista = []
n = int(input("Número: "))
while n != 0:
    lista.append(n)
    n = int(input("Número: "))

print("\nValores digitados: \n")
print(lista)
lista = remove_repetidos(lista)
print("\nLista sem elementos repetidos e ordenada: \n")
print(lista)
