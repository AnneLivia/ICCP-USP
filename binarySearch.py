def binary_search(lista, number, begin, end):
    if(begin > end):
        return False, -1
    mid = (begin) + (end - begin) // 2
    print(mid)
    if(lista[mid] == number):
        return True, mid
    if(lista[mid] < number):
        return binary_search(lista, number, mid + 1, end)
    else:
        return binary_search(lista, number, begin, mid - 1)
    

def busca(lista, element):
    begin = 0
    end = len(lista) - 1

    while(begin <= end):
        mid = begin + (end - begin) // 2
        print(mid)
        if(lista[mid] == element):
            return mid
        if(lista[mid] > element):
            end = mid - 1
        else:
            begin = mid + 1
    return False
        

#busca([1, 2, 3, 4, 5], 6)

