def menor_nome(liststr):
    strmenor = liststr[0].strip()
    for name in liststr:
        if(len(name.strip()) < len(strmenor)):
            strmenor = name.strip()
    return strmenor.lower().capitalize()
