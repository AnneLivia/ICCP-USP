def insertion_sort(lista):
    for i in range(1,len(lista)):
        j = i - 1
        element = lista[i]
        while(j >= 0 and lista[j + 1] < lista[j]):
            lista[j + 1], lista[j] = lista[j], lista[j + 1]
            j-=1    
        lista[j + 1] = element
    return lista
