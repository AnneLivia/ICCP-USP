def soma_elementos(lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma


lista = [7,8,65]
print("Valores da lista: \n\n")
print(lista)
soma = soma_elementos(lista)
print("Soma dos elementos: ",soma)
