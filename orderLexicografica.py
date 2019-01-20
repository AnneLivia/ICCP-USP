def primeiro_lex(lista):
    strm = lista[0]
    for st in lista:
        if(strm > st):
            strm = st
    return strm
