def conta_letras(frase, contar="vogais"):
    frase = frase.lower()
    qtdVogais, qtdConsoante = 0, 0
    for i in range(len(frase)):
            if(frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u'):
                qtdVogais+=1
            elif frase[i] != ' ':
                qtdConsoante+=1
    if contar != "vogais":
        return qtdConsoante
    else:
        return qtdVogais
        
