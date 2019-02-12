def ordena(lista):
    for i in range(len(lista) - 1):
        smaller = i
        for j in range(i + 1, len(lista)):
            if lista[smaller] > lista[j]:
                smaller = j
        lista[i], lista[smaller] = lista[smaller], lista[i]
    return lista

