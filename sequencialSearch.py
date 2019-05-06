def busca(lista, elemento):
    for i in range(len(lista)):
        if(lista[i] == elemento):
            return i
    return False

def main():
    lista = ['a','b','c','d']
    print("Letter 'c' is in the list: ", busca(lista,'c'))
    print("Letter 'd' is in the list: ", busca(lista,'d'))
    print("Letter 'z' is in the list: ", busca(lista,'z'))
